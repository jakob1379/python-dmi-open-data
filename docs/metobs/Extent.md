# Extent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spatial** | [**Spatial**](Spatial.md) |  | [optional] 
**temporal** | [**Temporal**](Temporal.md) |  | [optional] 

## Example

```python
from dmi_open_data.metobs.models.extent import Extent

# TODO update the JSON string below
json = "{}"
# create an instance of Extent from a JSON string
extent_instance = Extent.from_json(json)
# print the JSON string representation of the object
print(Extent.to_json())

# convert the object into a dict
extent_dict = extent_instance.to_dict()
# create an instance of Extent from a dict
extent_from_dict = Extent.from_dict(extent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


