# panviva.ResourcesApi

All URIs are relative to *https://api.panviva.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resources_artefact_by_id**](ResourcesApi.md#resources_artefact_by_id) | **GET** /{instance}/resources/artefact/{id} | Artefact
[**resources_artefact_categories_get**](ResourcesApi.md#resources_artefact_categories_get) | **GET** /{instance}/resources/artefactcategory | Get Artefact Categories
[**resources_artefact_category_post**](ResourcesApi.md#resources_artefact_category_post) | **POST** /{instance}/resources/artefactcategory | Create Artefact Category
[**resources_container_by_id**](ResourcesApi.md#resources_container_by_id) | **GET** /{instance}/resources/container/{id} | Container
[**resources_document_by_id**](ResourcesApi.md#resources_document_by_id) | **GET** /{instance}/resources/document/{id} | Document
[**resources_document_by_id_containers**](ResourcesApi.md#resources_document_by_id_containers) | **GET** /{instance}/resources/document/{id}/containers | Document Containers
[**resources_document_by_id_containers_relationships**](ResourcesApi.md#resources_document_by_id_containers_relationships) | **GET** /{instance}/resources/document/{id}/containers/relationships | Document Container Relationships
[**resources_document_by_id_translations**](ResourcesApi.md#resources_document_by_id_translations) | **GET** /{instance}/resources/document/{id}/translations | Document Translations
[**resources_file_by_id**](ResourcesApi.md#resources_file_by_id) | **GET** /{instance}/resources/file/{id} | File
[**resources_folder_by_id**](ResourcesApi.md#resources_folder_by_id) | **GET** /{instance}/resources/folder/{id} | Folder
[**resources_folder_by_id_children**](ResourcesApi.md#resources_folder_by_id_children) | **GET** /{instance}/resources/folder/{id}/children | Folder Children
[**resources_folder_by_id_translations**](ResourcesApi.md#resources_folder_by_id_translations) | **GET** /{instance}/resources/folder/{id}/translations | Folder Translations
[**resources_folder_root**](ResourcesApi.md#resources_folder_root) | **GET** /{instance}/resources/folder/root | Folder Root
[**resources_image_by_id**](ResourcesApi.md#resources_image_by_id) | **GET** /{instance}/resources/image/{id} | Image


# **resources_artefact_by_id**
> GetResponseResponse resources_artefact_by_id(instance, id)

Artefact

Return an artefact using the ID provided

### Example
```python
from __future__ import print_function
import time
import panviva
from panviva.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = panviva.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'

# create an instance of the API class
api_instance = panviva.ResourcesApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.
id = 'id_example' # str | Format - uuid. The id (ID) of an artefact

try:
    # Artefact
    api_response = api_instance.resources_artefact_by_id(instance, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_artefact_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 
 **id** | **str**| Format - uuid. The id (ID) of an artefact | 

### Return type

[**GetResponseResponse**](GetResponseResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_artefact_categories_get**
> GetArtefactCategoriesResponse resources_artefact_categories_get(instance)

Get Artefact Categories

Gets a list of all available artefact categories

### Example
```python
from __future__ import print_function
import time
import panviva
from panviva.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = panviva.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'

# create an instance of the API class
api_instance = panviva.ResourcesApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.

try:
    # Get Artefact Categories
    api_response = api_instance.resources_artefact_categories_get(instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_artefact_categories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 

### Return type

[**GetArtefactCategoriesResponse**](GetArtefactCategoriesResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_artefact_category_post**
> PostArtefactCategoryResponse resources_artefact_category_post(instance, post_artefact_category_request=post_artefact_category_request)

Create Artefact Category

Creates a category for classifying artefacts

### Example
```python
from __future__ import print_function
import time
import panviva
from panviva.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = panviva.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'

# create an instance of the API class
api_instance = panviva.ResourcesApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.
post_artefact_category_request = panviva.PostArtefactCategoryRequest() # PostArtefactCategoryRequest | JSON object containing the category name (optional)

try:
    # Create Artefact Category
    api_response = api_instance.resources_artefact_category_post(instance, post_artefact_category_request=post_artefact_category_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_artefact_category_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 
 **post_artefact_category_request** | [**PostArtefactCategoryRequest**](PostArtefactCategoryRequest.md)| JSON object containing the category name | [optional] 

### Return type

[**PostArtefactCategoryResponse**](PostArtefactCategoryResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_container_by_id**
> GetContainerResponse resources_container_by_id(instance, id)

Container

Return a container using the container ID provided

### Example
```python
from __future__ import print_function
import time
import panviva
from panviva.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = panviva.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'

# create an instance of the API class
api_instance = panviva.ResourcesApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.
id = 'id_example' # str | The id of a document container

try:
    # Container
    api_response = api_instance.resources_container_by_id(instance, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_container_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 
 **id** | **str**| The id of a document container | 

### Return type

[**GetContainerResponse**](GetContainerResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_document_by_id**
> GetDocumentResponse resources_document_by_id(instance, id, version=version)

Document

Return a document using the document ID provided

### Example
```python
from __future__ import print_function
import time
import panviva
from panviva.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = panviva.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'

# create an instance of the API class
api_instance = panviva.ResourcesApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.
id = 'id_example' # str | A document unique identifier, Document ID. If a document is a translated document, this value represents Internal ID or IID in Panviva API v1.
version = 56 # int | Request the API to return a particular version of the specified document. (optional)

try:
    # Document
    api_response = api_instance.resources_document_by_id(instance, id, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_document_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 
 **id** | **str**| A document unique identifier, Document ID. If a document is a translated document, this value represents Internal ID or IID in Panviva API v1. | 
 **version** | **int**| Request the API to return a particular version of the specified document. | [optional] 

### Return type

[**GetDocumentResponse**](GetDocumentResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_document_by_id_containers**
> GetDocumentContainersResponse resources_document_by_id_containers(instance, id)

Document Containers

Return a list of containers using the document ID provided

### Example
```python
from __future__ import print_function
import time
import panviva
from panviva.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = panviva.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'

# create an instance of the API class
api_instance = panviva.ResourcesApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.
id = 56 # int | The internal id (IID) of a Panviva document

try:
    # Document Containers
    api_response = api_instance.resources_document_by_id_containers(instance, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_document_by_id_containers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 
 **id** | **int**| The internal id (IID) of a Panviva document | 

### Return type

[**GetDocumentContainersResponse**](GetDocumentContainersResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_document_by_id_containers_relationships**
> GetDocumentContainerRelationshipsResponse resources_document_by_id_containers_relationships(instance, id)

Document Container Relationships

Return a list of the parent-child relationship between each container for the document ID provided

### Example
```python
from __future__ import print_function
import time
import panviva
from panviva.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = panviva.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'

# create an instance of the API class
api_instance = panviva.ResourcesApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.
id = 56 # int | The internal id (IID) of a Panviva document

try:
    # Document Container Relationships
    api_response = api_instance.resources_document_by_id_containers_relationships(instance, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_document_by_id_containers_relationships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 
 **id** | **int**| The internal id (IID) of a Panviva document | 

### Return type

[**GetDocumentContainerRelationshipsResponse**](GetDocumentContainerRelationshipsResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_document_by_id_translations**
> GetDocumentTranslationsResponse resources_document_by_id_translations(instance, id)

Document Translations

Return a list of all translations (per language and locale) of a Panviva document

### Example
```python
from __future__ import print_function
import time
import panviva
from panviva.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = panviva.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'

# create an instance of the API class
api_instance = panviva.ResourcesApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.
id = 56 # int | The internal id (IID) of a Panviva document.

try:
    # Document Translations
    api_response = api_instance.resources_document_by_id_translations(instance, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_document_by_id_translations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 
 **id** | **int**| The internal id (IID) of a Panviva document. | 

### Return type

[**GetDocumentTranslationsResponse**](GetDocumentTranslationsResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_file_by_id**
> GetFileResponse resources_file_by_id(instance, id)

File

Returns a file (external document) from Panviva

### Example
```python
from __future__ import print_function
import time
import panviva
from panviva.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = panviva.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'

# create an instance of the API class
api_instance = panviva.ResourcesApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.
id = 56 # int | The internal id (IID) of a Panviva file (external document)

try:
    # File
    api_response = api_instance.resources_file_by_id(instance, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_file_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 
 **id** | **int**| The internal id (IID) of a Panviva file (external document) | 

### Return type

[**GetFileResponse**](GetFileResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_folder_by_id**
> GetFolderResponse resources_folder_by_id(instance, id)

Folder

Return information about a Panviva folder and references to each of its direct children

### Example
```python
from __future__ import print_function
import time
import panviva
from panviva.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = panviva.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'

# create an instance of the API class
api_instance = panviva.ResourcesApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.
id = 56 # int | The internal id (IID) of a Panviva folder

try:
    # Folder
    api_response = api_instance.resources_folder_by_id(instance, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_folder_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 
 **id** | **int**| The internal id (IID) of a Panviva folder | 

### Return type

[**GetFolderResponse**](GetFolderResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_folder_by_id_children**
> GetFolderChildrenResponse resources_folder_by_id_children(instance, id)

Folder Children

Gets all the immediate children of a Panviva folder, not including grandchildren. Children can be folders, documents, or files (external documents)

### Example
```python
from __future__ import print_function
import time
import panviva
from panviva.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = panviva.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'

# create an instance of the API class
api_instance = panviva.ResourcesApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.
id = 56 # int | The internal id (IID) of a Panviva folder

try:
    # Folder Children
    api_response = api_instance.resources_folder_by_id_children(instance, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_folder_by_id_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 
 **id** | **int**| The internal id (IID) of a Panviva folder | 

### Return type

[**GetFolderChildrenResponse**](GetFolderChildrenResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_folder_by_id_translations**
> GetFolderTranslationsResponse resources_folder_by_id_translations(instance, id)

Folder Translations

Gets all the translations of a Panviva folder, along with each translated folders respective children

### Example
```python
from __future__ import print_function
import time
import panviva
from panviva.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = panviva.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'

# create an instance of the API class
api_instance = panviva.ResourcesApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.
id = 56 # int | The internal id (IID) of a Panviva folder

try:
    # Folder Translations
    api_response = api_instance.resources_folder_by_id_translations(instance, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_folder_by_id_translations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 
 **id** | **int**| The internal id (IID) of a Panviva folder | 

### Return type

[**GetFolderTranslationsResponse**](GetFolderTranslationsResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_folder_root**
> GetFolderRootResponse resources_folder_root(instance)

Folder Root

Gets the root/home folder in all of Panviva, which can be drilled into using the Get Folder Children endpoint. Note this endpoint was formerly referred to as the 'Folder Search' endpoint

### Example
```python
from __future__ import print_function
import time
import panviva
from panviva.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = panviva.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'

# create an instance of the API class
api_instance = panviva.ResourcesApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.

try:
    # Folder Root
    api_response = api_instance.resources_folder_root(instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_folder_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 

### Return type

[**GetFolderRootResponse**](GetFolderRootResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_image_by_id**
> GetImageResponse resources_image_by_id(instance, id)

Image

Returns an image from Panviva. Image data is represented as a base64 string

### Example
```python
from __future__ import print_function
import time
import panviva
from panviva.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = panviva.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'

# create an instance of the API class
api_instance = panviva.ResourcesApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.
id = 56 # int | The id of a Panviva image

try:
    # Image
    api_response = api_instance.resources_image_by_id(instance, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_image_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 
 **id** | **int**| The id of a Panviva image | 

### Return type

[**GetImageResponse**](GetImageResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

