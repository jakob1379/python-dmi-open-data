# coding: utf-8

# flake8: noqa

"""
    DMI Open Data API - Met observation

    <h2>Free access to the Danish Meteorological Institutes data.  <img style=\"float: right; max-width: 6%;\" src='https://www.dmi.dk/fileadmin/templates/img/logo.png'></img></h2>                    <p>The services provided by this API require authentication and an authentication key is mandatory.<br/>In order to retrieve data it is necessary to register as user. Read more here: <a style=\"text-decoration: none;\" href=\"https://opendatadocs.dmi.govcloud.dk/en/Authentication\">Authentication</a></p>                    <p><a style=\"text-decoration: none;\" href=\"https://opendatadocs.dmi.govcloud.dk/en/APIs/Meteorological_Observation_API\">Information about the Meteorological Observation service</a></p>                    <p>This service follows the standard for OGC API Features as described in <a href=\"https://docs.opengeospatial.org/is/17-069r3/17-069r3.html\">OGC API - Features - Part 1: Core</a></p>

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from dmi_open_data.metobs.api.capabilities_api import CapabilitiesApi
from dmi_open_data.metobs.api.met_observation_api import MetObservationApi
from dmi_open_data.metobs.api.met_station_api import MetStationApi

# import ApiClient
from dmi_open_data.metobs.api_response import ApiResponse
from dmi_open_data.metobs.api_client import ApiClient
from dmi_open_data.metobs.configuration import Configuration
from dmi_open_data.metobs.exceptions import OpenApiException
from dmi_open_data.metobs.exceptions import ApiTypeError
from dmi_open_data.metobs.exceptions import ApiValueError
from dmi_open_data.metobs.exceptions import ApiKeyError
from dmi_open_data.metobs.exceptions import ApiAttributeError
from dmi_open_data.metobs.exceptions import ApiException

# import models into sdk package
from dmi_open_data.metobs.models.collection import Collection
from dmi_open_data.metobs.models.collections import Collections
from dmi_open_data.metobs.models.conformance import Conformance
from dmi_open_data.metobs.models.extent import Extent
from dmi_open_data.metobs.models.feature import Feature
from dmi_open_data.metobs.models.feature_collection import FeatureCollection
from dmi_open_data.metobs.models.geometry import Geometry
from dmi_open_data.metobs.models.landing_page import LandingPage
from dmi_open_data.metobs.models.link import Link
from dmi_open_data.metobs.models.spatial import Spatial
from dmi_open_data.metobs.models.temporal import Temporal
