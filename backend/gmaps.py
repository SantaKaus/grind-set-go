import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

class GMaps:
  def __init__(self, api_key):
    self.api_key = api_key
    self.base_url = "https://places.googleapis.com/v1/places"

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
        'X-Goog-FieldMask': 'places.id,places.name'  # Only retrieve place_id and name
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

    response = requests.post(self.base_url + ":searchText", headers=headers, json=data)

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


    response = requests.get(f"{self.base_url}/{place_id}", headers=headers)

    if response.status_code == 200:
      return response.json()
    else:
      return f"Error: {response.status_code}, {response.text}"

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
  min_rating=4.0,  # Only cafes with a rating of 4 or higher
)

if isinstance(text_search_results, dict):
  place_id = text_search_results.get("places", [])[0].get("id")
  # Get Place Details
  place_details = gmaps_client.place_details(place_id)
  print(place_details)
  if isinstance(place_details, dict):
    print(place_details)


