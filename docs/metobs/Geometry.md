# Geometry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**bbox** | **List[float]** |  | [optional] 

## Example

```python
from dmi_open_data.metobs.models.geometry import Geometry

# TODO update the JSON string below
json = "{}"
# create an instance of Geometry from a JSON string
geometry_instance = Geometry.from_json(json)
# print the JSON string representation of the object
print(Geometry.to_json())

# convert the object into a dict
geometry_dict = geometry_instance.to_dict()
# create an instance of Geometry from a dict
geometry_from_dict = Geometry.from_dict(geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


