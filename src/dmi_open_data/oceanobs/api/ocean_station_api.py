# coding: utf-8

"""
    DMI Open Data API - Ocean observation

    <h2>Free access to the Danish Meteorological Institutes data.  <img style=\"float: right; max-width: 6%;\" src='https://www.dmi.dk/fileadmin/templates/img/logo.png'></img></h2>                    <p>The services provided by this API require authentication and an authentication key is mandatory.<br/>In order to retrieve data it is necessary to register as user. Read more here: <a style=\"text-decoration: none;\" href=\"https://opendatadocs.dmi.govcloud.dk/en/Authentication\">Authentication</a></p>                    <p><a style=\"text-decoration: none;\" href=\"https://opendatadocs.dmi.govcloud.dk/en/APIs/Oceanographic_Observation_API\">Information about the Oceanographic Observation service</a></p>                    <p>This service follows the standard for OGC API Features as described in <a href=\"https://docs.opengeospatial.org/is/17-069r3/17-069r3.html\">OGC API - Features - Part 1: Core</a></p>

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import List, Optional, Union
from typing_extensions import Annotated
from dmi_open_data.oceanobs.models.feature import Feature
from dmi_open_data.oceanobs.models.feature_collection import FeatureCollection

from dmi_open_data.oceanobs.api_client import ApiClient, RequestSerialized
from dmi_open_data.oceanobs.api_response import ApiResponse
from dmi_open_data.oceanobs.rest import RESTResponseType


class OceanStationApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_station_by_id1(
        self,
        id: Annotated[str, Field(strict=True)],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Feature:
        """Get a single station


        :param id: (required)
        :type id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_station_by_id1_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Feature",
            '5XX': None,
            '4XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_station_by_id1_with_http_info(
        self,
        id: Annotated[str, Field(strict=True)],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Feature]:
        """Get a single station


        :param id: (required)
        :type id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_station_by_id1_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Feature",
            '5XX': None,
            '4XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_station_by_id1_without_preload_content(
        self,
        id: Annotated[str, Field(strict=True)],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get a single station


        :param id: (required)
        :type id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_station_by_id1_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Feature",
            '5XX': None,
            '4XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_station_by_id1_serialize(
        self,
        id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'api-key'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v2/oceanObs/collections/station/items/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_stations1(
        self,
        datetime: Annotated[Optional[StrictStr], Field(description="datetime searching as specified in https://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_parameter_datetime  an dates as specified in RFC3339 https://tools.ietf.org/html/rfc3339")] = None,
        station_id: Annotated[Optional[StrictStr], Field(description="Filter by stationId")] = None,
        status: Annotated[Optional[StrictStr], Field(description="Filter results by station status. Status can be either Active or Inactive. See station list <a href=\"https://opendatadocs.dmi.govcloud.dk/Data/Oceanographic_Observation_Data_Stations\">here</a>")] = None,
        type: Annotated[Optional[StrictStr], Field(description="Filter by station type")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=300000, strict=True, ge=1)]], Field(description="Maximum number of results to return")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="number of results to skip before returning matching results")] = None,
        bbox: Annotated[Optional[Annotated[List[Union[StrictFloat, StrictInt]], Field(min_length=4, max_length=6)]], Field(description="Select stations within bounding box. Southwesterly point (lon,lat) followed by northeasterly point (lon, lat)")] = None,
        bbox_crs: Annotated[Optional[StrictStr], Field(description="Which coordinate reference system to use. Only the CRS84 is supported")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> FeatureCollection:
        """Get stations


        :param datetime: datetime searching as specified in https://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_parameter_datetime  an dates as specified in RFC3339 https://tools.ietf.org/html/rfc3339
        :type datetime: str
        :param station_id: Filter by stationId
        :type station_id: str
        :param status: Filter results by station status. Status can be either Active or Inactive. See station list <a href=\"https://opendatadocs.dmi.govcloud.dk/Data/Oceanographic_Observation_Data_Stations\">here</a>
        :type status: str
        :param type: Filter by station type
        :type type: str
        :param limit: Maximum number of results to return
        :type limit: int
        :param offset: number of results to skip before returning matching results
        :type offset: int
        :param bbox: Select stations within bounding box. Southwesterly point (lon,lat) followed by northeasterly point (lon, lat)
        :type bbox: List[float]
        :param bbox_crs: Which coordinate reference system to use. Only the CRS84 is supported
        :type bbox_crs: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_stations1_serialize(
            datetime=datetime,
            station_id=station_id,
            status=status,
            type=type,
            limit=limit,
            offset=offset,
            bbox=bbox,
            bbox_crs=bbox_crs,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FeatureCollection",
            '5XX': None,
            '4XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_stations1_with_http_info(
        self,
        datetime: Annotated[Optional[StrictStr], Field(description="datetime searching as specified in https://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_parameter_datetime  an dates as specified in RFC3339 https://tools.ietf.org/html/rfc3339")] = None,
        station_id: Annotated[Optional[StrictStr], Field(description="Filter by stationId")] = None,
        status: Annotated[Optional[StrictStr], Field(description="Filter results by station status. Status can be either Active or Inactive. See station list <a href=\"https://opendatadocs.dmi.govcloud.dk/Data/Oceanographic_Observation_Data_Stations\">here</a>")] = None,
        type: Annotated[Optional[StrictStr], Field(description="Filter by station type")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=300000, strict=True, ge=1)]], Field(description="Maximum number of results to return")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="number of results to skip before returning matching results")] = None,
        bbox: Annotated[Optional[Annotated[List[Union[StrictFloat, StrictInt]], Field(min_length=4, max_length=6)]], Field(description="Select stations within bounding box. Southwesterly point (lon,lat) followed by northeasterly point (lon, lat)")] = None,
        bbox_crs: Annotated[Optional[StrictStr], Field(description="Which coordinate reference system to use. Only the CRS84 is supported")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[FeatureCollection]:
        """Get stations


        :param datetime: datetime searching as specified in https://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_parameter_datetime  an dates as specified in RFC3339 https://tools.ietf.org/html/rfc3339
        :type datetime: str
        :param station_id: Filter by stationId
        :type station_id: str
        :param status: Filter results by station status. Status can be either Active or Inactive. See station list <a href=\"https://opendatadocs.dmi.govcloud.dk/Data/Oceanographic_Observation_Data_Stations\">here</a>
        :type status: str
        :param type: Filter by station type
        :type type: str
        :param limit: Maximum number of results to return
        :type limit: int
        :param offset: number of results to skip before returning matching results
        :type offset: int
        :param bbox: Select stations within bounding box. Southwesterly point (lon,lat) followed by northeasterly point (lon, lat)
        :type bbox: List[float]
        :param bbox_crs: Which coordinate reference system to use. Only the CRS84 is supported
        :type bbox_crs: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_stations1_serialize(
            datetime=datetime,
            station_id=station_id,
            status=status,
            type=type,
            limit=limit,
            offset=offset,
            bbox=bbox,
            bbox_crs=bbox_crs,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FeatureCollection",
            '5XX': None,
            '4XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_stations1_without_preload_content(
        self,
        datetime: Annotated[Optional[StrictStr], Field(description="datetime searching as specified in https://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_parameter_datetime  an dates as specified in RFC3339 https://tools.ietf.org/html/rfc3339")] = None,
        station_id: Annotated[Optional[StrictStr], Field(description="Filter by stationId")] = None,
        status: Annotated[Optional[StrictStr], Field(description="Filter results by station status. Status can be either Active or Inactive. See station list <a href=\"https://opendatadocs.dmi.govcloud.dk/Data/Oceanographic_Observation_Data_Stations\">here</a>")] = None,
        type: Annotated[Optional[StrictStr], Field(description="Filter by station type")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=300000, strict=True, ge=1)]], Field(description="Maximum number of results to return")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="number of results to skip before returning matching results")] = None,
        bbox: Annotated[Optional[Annotated[List[Union[StrictFloat, StrictInt]], Field(min_length=4, max_length=6)]], Field(description="Select stations within bounding box. Southwesterly point (lon,lat) followed by northeasterly point (lon, lat)")] = None,
        bbox_crs: Annotated[Optional[StrictStr], Field(description="Which coordinate reference system to use. Only the CRS84 is supported")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get stations


        :param datetime: datetime searching as specified in https://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_parameter_datetime  an dates as specified in RFC3339 https://tools.ietf.org/html/rfc3339
        :type datetime: str
        :param station_id: Filter by stationId
        :type station_id: str
        :param status: Filter results by station status. Status can be either Active or Inactive. See station list <a href=\"https://opendatadocs.dmi.govcloud.dk/Data/Oceanographic_Observation_Data_Stations\">here</a>
        :type status: str
        :param type: Filter by station type
        :type type: str
        :param limit: Maximum number of results to return
        :type limit: int
        :param offset: number of results to skip before returning matching results
        :type offset: int
        :param bbox: Select stations within bounding box. Southwesterly point (lon,lat) followed by northeasterly point (lon, lat)
        :type bbox: List[float]
        :param bbox_crs: Which coordinate reference system to use. Only the CRS84 is supported
        :type bbox_crs: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_stations1_serialize(
            datetime=datetime,
            station_id=station_id,
            status=status,
            type=type,
            limit=limit,
            offset=offset,
            bbox=bbox,
            bbox_crs=bbox_crs,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FeatureCollection",
            '5XX': None,
            '4XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_stations1_serialize(
        self,
        datetime,
        station_id,
        status,
        type,
        limit,
        offset,
        bbox,
        bbox_crs,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'bbox': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if datetime is not None:
            
            _query_params.append(('datetime', datetime))
            
        if station_id is not None:
            
            _query_params.append(('stationId', station_id))
            
        if status is not None:
            
            _query_params.append(('status', status))
            
        if type is not None:
            
            _query_params.append(('type', type))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if offset is not None:
            
            _query_params.append(('offset', offset))
            
        if bbox is not None:
            
            _query_params.append(('bbox', bbox))
            
        if bbox_crs is not None:
            
            _query_params.append(('bbox-crs', bbox_crs))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'api-key'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v2/oceanObs/collections/station/items',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


