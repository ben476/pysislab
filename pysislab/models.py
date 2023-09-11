from typing import List, Optional

from pydantic import BaseModel

class Geometry(BaseModel):
    type: str
    coordinates: List[float]

class Context(BaseModel):
    id: str
    mapbox_id: str
    text: str
    wikidata: Optional[str] = None
    short_code: Optional[str] = None

class GeoFeatures(BaseModel):
    id: str
    type: str
    place_type: List[str]
    relevance: int
    text: str
    place_name: str
    bbox: Optional[List[float]] = None
    center: List[float]
    geometry: Geometry
    context: List[Context]
    address: Optional[str] = None

class Sensor(BaseModel):
    id: int
    type: Optional[str] = None
    publicLocation: Optional[List[float]] = None
    online: bool
    timestamp: int
    publicGeoFeatures: Optional[GeoFeatures] = None
    secondary_id: str