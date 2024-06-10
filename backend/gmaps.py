import requests
import os
import json
from dotenv import load_dotenv
from classes import *
load_dotenv()

class GMaps:
  def __init__(self, api_key):
    self.api_key = api_key
    self.base_url = "https://places.googleapis.com/v1/"
    self.gmaps_details = None

  def text_search(self, query, included_type, latitude, longitude, radius=500, rank_preference="RELEVANCE", min_rating=None, strict_type_filtering=True):
    """
    Performs a Text Search on Google Places API (new version)

    Args:
      query: The text string to search for (e.g., "restaurants").
      included_type: The type of place to search for (e.g., "restaurant").
      latitude: The latitude of the search center.
      longitude: The longitude of the search center.
      radius: The radius of the search area in meters (default: 500).
      rank_preference: The preference for ranking results (default: RELEVANCE).
      min_rating: Minimum rating filter (optional).
      strict_type_filtering: Enforce strict type filtering (default: True).

    Returns:
      A dictionary containing the search results or an error message.
    """

    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': self.api_key,
        'X-Goog-FieldMask': 'places.id,places.name'
    }

    location_bias = {
      "circle": {
        "center": {
          "latitude": latitude,
          "longitude": longitude
        },
        "radius": radius
      }
    }

    data = {
      'textQuery': query,
      'includedType': included_type,
      'locationBias': location_bias,
      'rankPreference': rank_preference,
    }

    # Add optional parameters if provided
    if min_rating:
      data['minRating'] = min_rating
      data['strictTypeFiltering'] = strict_type_filtering

    response = requests.post(self.base_url + "places:searchText", headers=headers, json=data)

    if response.status_code == 200:
      return response.json()
    else:
      return f"Error: {response.status_code}, {response.text}"
    
  def place_details(self, place_id):
    """
    Retrieves details for a specific place using Google Places API (new version)

    Args:
    place_id: The unique identifier of the place.

    Returns:
    A dictionary containing the place details or an error message.
    """

    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': self.api_key,
        'X-Goog-FieldMask': 'displayName,dineIn,editorialSummary,goodForGroups,outdoorSeating,restroom,reviews,servesCoffee,currentOpeningHours,priceLevel,rating,userRatingCount,regularOpeningHours,addressComponents,formattedAddress,location,shortFormattedAddress,photos,types,primaryType,googleMapsUri'
    }


    response = requests.get(f"{self.base_url}places/{place_id}", headers=headers)

    if response.status_code == 200:
      return response.json()
    else:
      return f"Error: {response.status_code}, {response.text}"
  
  def load_gmaps_details_from_json(self, data, place_id):
    gmaps_details = GMapsDetails(
        id = place_id,
        types=data['types'],
        formattedAddress=data['formattedAddress'],
        addressComponents=[AddressComponent(**comp) for comp in data['addressComponents']],
        location=Location(**data['location']),
        rating=data['rating'],
        googleMapsUri=data['googleMapsUri'],
        regularOpeningHours=OpeningHours(**data['regularOpeningHours']),
        priceLevel=data['priceLevel'],
        userRatingCount=data['userRatingCount'],
        displayName=DisplayName(**data['displayName']),
        dineIn=data['dineIn'],
        currentOpeningHours=OpeningHours(**data['currentOpeningHours']),
        primaryType=data['primaryType'],
        shortFormattedAddress=data['shortFormattedAddress'],
        editorialSummary=DisplayName(**data['editorialSummary']),
        reviews=[Review(**review) for review in data['reviews']],
        photos=[Photo(**photo) for photo in data['photos']],
        outdoorSeating=data['outdoorSeating'],
        servesCoffee=data['servesCoffee'],
        restroom=data['restroom']
    )
    self.gmaps_details = gmaps_details

  def download_photos(self, max_width=400):
    """
    Downloads photos for a place and stores them in a directory.

    Args:
        place_id: The unique identifier of the place.
        photos: List of photo metadata from place details.
        max_width: The maximum width of the photos (default: 400).
    """
    directory = os.path.join('test_data', 'images', self.gmaps_details.id)
    os.makedirs(directory, exist_ok=True)

    for idx, photo in enumerate(self.gmaps_details.photos):
        photo_url = f"{self.base_url}{photo.name}/media?key={self.api_key}&maxWidthPx={max_width}"
        photo_response = requests.get(photo_url)
        if photo_response.status_code == 200:
            with open(os.path.join(directory, f"photo_{idx+1}.jpg"), 'wb') as file:
                file.write(photo_response.content)
        else:
            print(f"Failed to download photo {idx+1}: {photo_response.status_code}. Error: {photo_response.text}")


# -----------------------------------------------
# EXAMPLE USAGE
# -----------------------------------------------
# Get Text Search Results
gmaps_client = GMaps(os.getenv("GMAPS_API_KEY"))
text_search_results = gmaps_client.text_search(
  "voyager coffee",
  "cafe",
  latitude=37.7749,
  longitude=-122.4194,
  min_rating=4.0,
)

if isinstance(text_search_results, dict):
  place_id = text_search_results.get("places", [])[0].get("id")
  gmaps_details = gmaps_client.place_details(place_id)
  if isinstance(gmaps_details, dict):
    gmaps_client.load_gmaps_details_from_json(gmaps_details, place_id)
    gmaps_client.download_photos()