from typing import List, Optional
from enum import Enum
from datetime import datetime
from dataclasses import dataclass
from dataclasses_json import dataclass_json

class AddressComponent:
    longText: str
    shortText: str
    types: List[str]
    languageCode: str

    def __init__(self, longText: str, shortText: str, types: List[str], languageCode: str) -> None:
        self.longText = longText
        self.shortText = shortText
        self.types = types
        self.languageCode = languageCode


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
    openNow: str
    periods: List[Period]
    weekdayDescriptions: List[str]

    def __init__(self, openNow: str, periods: List[Period], weekdayDescriptions: List[str]) -> None:
        self.openNow = openNow
        self.periods = periods
        self.weekdayDescriptions = weekdayDescriptions


class LanguageCode(Enum):
    EN = "en"


class DisplayName:
    text: str
    languageCode: LanguageCode

    def __init__(self, text: str, languageCode: LanguageCode) -> None:
        self.text = text
        self.languageCode = languageCode


class Location:
    latitude: float
    longitude: float

    def __init__(self, latitude: float, longitude: float) -> None:
        self.latitude = latitude
        self.longitude = longitude


class AuthorAttribution:
    displayName: str
    uri: str
    photoUri: str

    def __init__(self, displayName: str, uri: str, photoUri: str) -> None:
        self.displayName = displayName
        self.uri = uri
        self.photoUri = photoUri


class Photo:
    name: str
    widthPx: int
    heightPx: int
    authorAttributions: List[AuthorAttribution]

    def __init__(self, name: str, widthPx: int, heightPx: int, authorAttributions: List[AuthorAttribution]) -> None:
        self.name = name
        self.widthPx = widthPx
        self.heightPx = heightPx
        self.authorAttributions = authorAttributions


class Review:
    name: str
    relativePublishTimeDescription: str
    rating: int
    text: DisplayName
    originalText: DisplayName
    authorAttribution: AuthorAttribution
    publishTime: datetime

    def __init__(self, name: str, relativePublishTimeDescription: str, rating: int, text: DisplayName, originalText: DisplayName, authorAttribution: AuthorAttribution, publishTime: datetime) -> None:
        self.name = name
        self.relativePublishTimeDescription = relativePublishTimeDescription
        self.rating = rating
        self.text = text
        self.originalText = originalText
        self.authorAttribution = authorAttribution
        self.publishTime = publishTime


class GMapsDetails:
    id: str
    types: List[str]
    formattedAddress: str
    addressComponents: List[AddressComponent]
    location: Location
    rating: float
    googleMapsUri: str
    regularOpeningHours: OpeningHours
    priceLevel: str
    userRatingCount: int
    displayName: DisplayName
    dineIn: str
    currentOpeningHours: OpeningHours
    primaryType: str
    shortFormattedAddress: str
    editorialSummary: DisplayName
    reviews: List[Review]
    photos: List[Photo]
    outdoorSeating: str
    servesCoffee: str
    restroom: str

    def __init__(self, id: str, types: List[str], formattedAddress: str, addressComponents: List[AddressComponent], location: Location, rating: float, googleMapsUri: str, regularOpeningHours: OpeningHours, priceLevel: str, userRatingCount: int, displayName: DisplayName, dineIn: str, currentOpeningHours: OpeningHours, primaryType: str, shortFormattedAddress: str, editorialSummary: DisplayName, reviews: List[Review], photos: List[Photo], outdoorSeating: str, servesCoffee: str, restroom: str) -> None:
        self.id = id
        self.types = types
        self.formattedAddress = formattedAddress
        self.addressComponents = addressComponents
        self.location = location
        self.rating = rating
        self.googleMapsUri = googleMapsUri
        self.regularOpeningHours = regularOpeningHours
        self.priceLevel = priceLevel
        self.userRatingCount = userRatingCount
        self.displayName = displayName
        self.dineIn = dineIn
        self.currentOpeningHours = currentOpeningHours
        self.primaryType = primaryType
        self.shortFormattedAddress = shortFormattedAddress
        self.editorialSummary = editorialSummary
        self.reviews = reviews
        self.photos = photos
        self.outdoorSeating = outdoorSeating
        self.servesCoffee = servesCoffee
        self.restroom = restroom

class Place:
    id: int
    gMapsDetails: GMapsDetails
    photos: List[str]

