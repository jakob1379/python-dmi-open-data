# Collections


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[Link]**](Link.md) |  | [optional] 
**collections** | [**List[Collection]**](Collection.md) |  | [optional] 

## Example

```python
from dmi_open_data.climatedata.models.collections import Collections

# TODO update the JSON string below
json = "{}"
# create an instance of Collections from a JSON string
collections_instance = Collections.from_json(json)
# print the JSON string representation of the object
print(Collections.to_json())

# convert the object into a dict
collections_dict = collections_instance.to_dict()
# create an instance of Collections from a dict
collections_from_dict = Collections.from_dict(collections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


