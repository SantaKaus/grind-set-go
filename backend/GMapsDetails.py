from typing import List, Optional
from enum import Enum
from datetime import datetime


class AddressComponent:
    long_text: str
    short_text: str
    types: List[str]
    language_code: str

    def __init__(self, long_text: str, short_text: str, types: List[str], language_code: str) -> None:
        self.long_text = long_text
        self.short_text = short_text
        self.types = types
        self.language_code = language_code


class Date:
    year: int
    month: int
    day: int

    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day


class Close:
    day: int
    hour: int
    minute: int
    date: Optional[Date]

    def __init__(self, day: int, hour: int, minute: int, date: Optional[Date]) -> None:
        self.day = day
        self.hour = hour
        self.minute = minute
        self.date = date


class Period:
    open: Close
    close: Close

    def __init__(self, open: Close, close: Close) -> None:
        self.open = open
        self.close = close


class OpeningHours:
    open_now: str
    periods: List[Period]
    weekday_descriptions: List[str]

    def __init__(self, open_now: str, periods: List[Period], weekday_descriptions: List[str]) -> None:
        self.open_now = open_now
        self.periods = periods
        self.weekday_descriptions = weekday_descriptions


class LanguageCode(Enum):
    EN = "en"


class DisplayName:
    text: str
    language_code: LanguageCode

    def __init__(self, text: str, language_code: LanguageCode) -> None:
        self.text = text
        self.language_code = language_code


class Location:
    latitude: float
    longitude: float

    def __init__(self, latitude: float, longitude: float) -> None:
        self.latitude = latitude
        self.longitude = longitude


class AuthorAttribution:
    display_name: str
    uri: str
    photo_uri: str

    def __init__(self, display_name: str, uri: str, photo_uri: str) -> None:
        self.display_name = display_name
        self.uri = uri
        self.photo_uri = photo_uri


class Photo:
    name: str
    width_px: int
    height_px: int
    author_attributions: List[AuthorAttribution]

    def __init__(self, name: str, width_px: int, height_px: int, author_attributions: List[AuthorAttribution]) -> None:
        self.name = name
        self.width_px = width_px
        self.height_px = height_px
        self.author_attributions = author_attributions


class Review:
    name: str
    relative_publish_time_description: str
    rating: int
    text: DisplayName
    original_text: DisplayName
    author_attribution: AuthorAttribution
    publish_time: datetime

    def __init__(self, name: str, relative_publish_time_description: str, rating: int, text: DisplayName, original_text: DisplayName, author_attribution: AuthorAttribution, publish_time: datetime) -> None:
        self.name = name
        self.relative_publish_time_description = relative_publish_time_description
        self.rating = rating
        self.text = text
        self.original_text = original_text
        self.author_attribution = author_attribution
        self.publish_time = publish_time


class GMapsDetails:
    types: List[str]
    formatted_address: str
    address_components: List[AddressComponent]
    location: Location
    rating: float
    google_maps_uri: str
    regular_opening_hours: OpeningHours
    price_level: str
    user_rating_count: int
    display_name: DisplayName
    dine_in: str
    current_opening_hours: OpeningHours
    primary_type: str
    short_formatted_address: str
    editorial_summary: DisplayName
    reviews: List[Review]
    photos: List[Photo]
    outdoor_seating: str
    serves_coffee: str
    restroom: str

    def __init__(self, types: List[str], formatted_address: str, address_components: List[AddressComponent], location: Location, rating: float, google_maps_uri: str, regular_opening_hours: OpeningHours, price_level: str, user_rating_count: int, display_name: DisplayName, dine_in: str, current_opening_hours: OpeningHours, primary_type: str, short_formatted_address: str, editorial_summary: DisplayName, reviews: List[Review], photos: List[Photo], outdoor_seating: str, serves_coffee: str, restroom: str) -> None:
        self.types = types
        self.formatted_address = formatted_address
        self.address_components = address_components
        self.location = location
        self.rating = rating
        self.google_maps_uri = google_maps_uri
        self.regular_opening_hours = regular_opening_hours
        self.price_level = price_level
        self.user_rating_count = user_rating_count
        self.display_name = display_name
        self.dine_in = dine_in
        self.current_opening_hours = current_opening_hours
        self.primary_type = primary_type
        self.short_formatted_address = short_formatted_address
        self.editorial_summary = editorial_summary
        self.reviews = reviews
        self.photos = photos
        self.outdoor_seating = outdoor_seating
        self.serves_coffee = serves_coffee
        self.restroom = restroom
