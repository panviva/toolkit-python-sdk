# panviva.OperationsApi

All URIs are relative to *https://api.panviva.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operations_artefact_nls**](OperationsApi.md#operations_artefact_nls) | **GET** /{instance}/operations/artefact/nls | Search Artefacts
[**operations_live_csh**](OperationsApi.md#operations_live_csh) | **POST** /{instance}/operations/live/csh | Live CSH
[**operations_live_document**](OperationsApi.md#operations_live_document) | **POST** /{instance}/operations/live/document | Live Document
[**operations_live_search**](OperationsApi.md#operations_live_search) | **POST** /{instance}/operations/live/search | Live Search
[**operations_search**](OperationsApi.md#operations_search) | **GET** /{instance}/operations/search | Search


# **operations_artefact_nls**
> GetSearchArtefactResponse operations_artefact_nls(instance, simplequery=simplequery, advancedquery=advancedquery, filter=filter, channel=channel, page_offset=page_offset, page_limit=page_limit, facet=facet)

Search Artefacts

Return search results for a given query

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
api_instance = panviva.OperationsApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.
simplequery = 'simplequery_example' # str | Natural language query string. For example: ```Action Movies```. (Note: Use simplequery OR advancedquery, not both.) (optional)
advancedquery = 'advancedquery_example' # str | Query string written in Lucene query syntax. For example: ```films AND \"a story\"```. (Note: Use simplequery OR advancedquery, not both.) (optional)
filter = 'filter_example' # str | Accepts a Lucene-formatted filter string. Examples: ```category eq 'Mortgages'```, ```panvivaDocumentVersion gt '8'```. (Filterable fields include dateCreated, dateModified, dateDeleted, categoryJson, queryVariationsJson, title, category, primaryQuery, isDeleted, timestamp, panvivaDocumentId, panvivaDocumentVersion, id) (optional)
channel = 'channel_example' # str | Return response for a specific channel, instead of the default (optional)
page_offset = 56 # int | The pagination offset to denote the number of initial search results to skip. For example, pageOffset of 100 and pageLimit of 10 would return records 101-110. (optional)
page_limit = 56 # int | The number of records to return. Must be an integer between 0 and 1000. (optional)
facet = 'facet_example' # str | Accepts a Lucene-formatted facet string. Examples: ```facet=Category,count:10&amp;facet=Rating```. (Facetable fields include metaData/values) (optional)

try:
    # Search Artefacts
    api_response = api_instance.operations_artefact_nls(instance, simplequery=simplequery, advancedquery=advancedquery, filter=filter, channel=channel, page_offset=page_offset, page_limit=page_limit, facet=facet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_artefact_nls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 
 **simplequery** | **str**| Natural language query string. For example: &#x60;&#x60;&#x60;Action Movies&#x60;&#x60;&#x60;. (Note: Use simplequery OR advancedquery, not both.) | [optional] 
 **advancedquery** | **str**| Query string written in Lucene query syntax. For example: &#x60;&#x60;&#x60;films AND \&quot;a story\&quot;&#x60;&#x60;&#x60;. (Note: Use simplequery OR advancedquery, not both.) | [optional] 
 **filter** | **str**| Accepts a Lucene-formatted filter string. Examples: &#x60;&#x60;&#x60;category eq &#39;Mortgages&#39;&#x60;&#x60;&#x60;, &#x60;&#x60;&#x60;panvivaDocumentVersion gt &#39;8&#39;&#x60;&#x60;&#x60;. (Filterable fields include dateCreated, dateModified, dateDeleted, categoryJson, queryVariationsJson, title, category, primaryQuery, isDeleted, timestamp, panvivaDocumentId, panvivaDocumentVersion, id) | [optional] 
 **channel** | **str**| Return response for a specific channel, instead of the default | [optional] 
 **page_offset** | **int**| The pagination offset to denote the number of initial search results to skip. For example, pageOffset of 100 and pageLimit of 10 would return records 101-110. | [optional] 
 **page_limit** | **int**| The number of records to return. Must be an integer between 0 and 1000. | [optional] 
 **facet** | **str**| Accepts a Lucene-formatted facet string. Examples: &#x60;&#x60;&#x60;facet&#x3D;Category,count:10&amp;amp;facet&#x3D;Rating&#x60;&#x60;&#x60;. (Facetable fields include metaData/values) | [optional] 

### Return type

[**GetSearchArtefactResponse**](GetSearchArtefactResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_live_csh**
> PostLiveCshResponse operations_live_csh(instance, post_live_csh_request=post_live_csh_request)

Live CSH

Present a CSH search result page of the passing query on Panviva client to specified user on Panviva client

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
api_instance = panviva.OperationsApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.
post_live_csh_request = panviva.PostLiveCshRequest() # PostLiveCshRequest | JSON object containing information required to perform a live activity<span>:</span> (optional)

try:
    # Live CSH
    api_response = api_instance.operations_live_csh(instance, post_live_csh_request=post_live_csh_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_live_csh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 
 **post_live_csh_request** | [**PostLiveCshRequest**](PostLiveCshRequest.md)| JSON object containing information required to perform a live activity&lt;span&gt;:&lt;/span&gt; | [optional] 

### Return type

[**PostLiveCshResponse**](PostLiveCshResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_live_document**
> PostLiveDocumentResponse operations_live_document(instance, post_live_document_request=post_live_document_request)

Live Document

Present a document page to specified user on Panviva client

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
api_instance = panviva.OperationsApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.
post_live_document_request = panviva.PostLiveDocumentRequest() # PostLiveDocumentRequest | JSON object containing information required to perform a live activity<span>:</span> (optional)

try:
    # Live Document
    api_response = api_instance.operations_live_document(instance, post_live_document_request=post_live_document_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_live_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 
 **post_live_document_request** | [**PostLiveDocumentRequest**](PostLiveDocumentRequest.md)| JSON object containing information required to perform a live activity&lt;span&gt;:&lt;/span&gt; | [optional] 

### Return type

[**PostLiveDocumentResponse**](PostLiveDocumentResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_live_search**
> PostLiveSearchResponse operations_live_search(instance, post_live_search_request=post_live_search_request)

Live Search

Present a search result page of the passing query on Panviva client to specified user on Panviva client

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
api_instance = panviva.OperationsApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.
post_live_search_request = panviva.PostLiveSearchRequest() # PostLiveSearchRequest | JSON object containing information required to perform a live activity<span>:</span> (optional)

try:
    # Live Search
    api_response = api_instance.operations_live_search(instance, post_live_search_request=post_live_search_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_live_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 
 **post_live_search_request** | [**PostLiveSearchRequest**](PostLiveSearchRequest.md)| JSON object containing information required to perform a live activity&lt;span&gt;:&lt;/span&gt; | [optional] 

### Return type

[**PostLiveSearchResponse**](PostLiveSearchResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operations_search**
> GetSearchResponse operations_search(instance, term, page_offset=page_offset, page_limit=page_limit)

Search

Searches documents, folders, and files (external documents) for a term and returns paginated results

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
api_instance = panviva.OperationsApi(panviva.ApiClient(configuration))
instance = 'instance_example' # str | The instance name as shown on the Panviva Developer Portal.
term = 'term_example' # str | The word or phrase to be searched for
page_offset = 56 # int | The pagination offset to denote the number of initial search results to skip. For example, pageOffset of 100 and pageLimit of 10 would return records 101-110. (optional)
page_limit = 56 # int | The number of records to return. Must be an integer between 0 and 1000. (optional)

try:
    # Search
    api_response = api_instance.operations_search(instance, term, page_offset=page_offset, page_limit=page_limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | **str**| The instance name as shown on the Panviva Developer Portal. | 
 **term** | **str**| The word or phrase to be searched for | 
 **page_offset** | **int**| The pagination offset to denote the number of initial search results to skip. For example, pageOffset of 100 and pageLimit of 10 would return records 101-110. | [optional] 
 **page_limit** | **int**| The number of records to return. Must be an integer between 0 and 1000. | [optional] 

### Return type

[**GetSearchResponse**](GetSearchResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

