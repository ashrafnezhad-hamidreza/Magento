import json, requests
from requests_oauthlib import OAuth1


def HeaderOAuth(client_key, client_secret, resource_owner_key, resource_owner_secret):
    return OAuth1(client_key, client_secret, resource_owner_key, resource_owner_secret, signature_type='auth_header')


def ProductJSON(**data: {}):
    # sample dictionary for creating product JSON.
    # if data be empty, a sample JSON based on bellow url will be returned.
    # http://devdocs.magento.com/swagger/index_21.html#!/catalogProductRepositoryV1/catalogProductRepositoryV1SavePut
    product_dict = {
        "id": data.get("id") or 0,
        "sku": data.get("sku") or "product sku",
        "name": data.get("name") or "product name",
        "attribute_set_id": data.get("attribute_set_id") or 0,
        "price": data.get("price") or 0,
        "status": data.get("status") or 0,
        "visibility": data.get("visibility") or 0,
        "type_id": data.get("type_id") or "product type_id",
        "created_at": data.get("created_at") or "product created_at",
        "updated_at": data.get("updated_at") or "product updated_at",
        "weight": data.get("weight") or 0,
        "extension_attributes": {
            "stock_item": data.get("extension_attributes").get("stock_item") or {
                "item_id": 0,
                "product_id": 0,
                "stock_id": 0,
                "qty": 0,
                "is_in_stock": True,
                "is_qty_decimal": True,
                "show_default_notification_message": True,
                "use_config_min_qty": True,
                "min_qty": 0,
                "use_config_min_sale_qty": 0,
                "min_sale_qty": 0,
                "use_config_max_sale_qty": True,
                "max_sale_qty": 0,
                "use_config_backorders": True,
                "backorders": 0,
                "use_config_notify_stock_qty": True,
                "notify_stock_qty": 0,
                "use_config_qty_increments": True,
                "qty_increments": 0,
                "use_config_enable_qty_inc": True,
                "enable_qty_increments": True,
                "use_config_manage_stock": True,
                "manage_stock": True,
                "low_stock_date": "product low_stock_date",
                "is_decimal_divided": True,
                "stock_status_changed_auto": 0,
                "extension_attributes": {}
            },
            "bundle_product_options": data.get("extension_attributes").get("bundle_product_options") or [
                {
                    "option_id": 0,
                    "title": "product title",
                    "required": True,
                    "type": "product type",
                    "position": 0,
                    "sku": "product sku",
                    "product_links": [
                        {
                            "id": "product id",
                            "sku": "product sku",
                            "option_id": 0,
                            "qty": 0,
                            "position": 0,
                            "is_default": True,
                            "price": 0,
                            "price_type": 0,
                            "can_change_quantity": 0,
                            "extension_attributes": {}
                        }
                    ],
                    "extension_attributes": {}
                }
            ],
            "downloadable_product_links": data.get("extension_attributes").get("downloadable_product_links") or [
                {
                    "id": 0,
                    "title": "product title",
                    "sort_order": 0,
                    "is_shareable": 0,
                    "price": 0,
                    "number_of_downloads": 0,
                    "link_type": "product link_type",
                    "link_file": "product link_file",
                    "link_file_content": {
                        "file_data": "product file_data",
                        "name": "product name",
                        "extension_attributes": {}
                    },
                    "link_url": "product link_url",
                    "sample_type": "product sample_type",
                    "sample_file": "product sample_file",
                    "sample_file_content": {
                        "file_data": "product file_data",
                        "name": "product name",
                        "extension_attributes": {}
                    },
                    "sample_url": "product sample_url",
                    "extension_attributes": {}
                }
            ],
            "downloadable_product_samples": data.get("extension_attributes").get("downloadable_product_samples") or [
                {
                    "id": 0,
                    "title": "product title",
                    "sort_order": 0,
                    "sample_type": "product sample_type",
                    "sample_file": "product sample_file",
                    "sample_file_content": {
                        "file_data": "product file_data",
                        "name": "product name",
                        "extension_attributes": {}
                    },
                    "sample_url": "product sample_url",
                    "extension_attributes": {}
                }
            ],
            "giftcard_amounts": data.get("extension_attributes").get("giftcard_amounts") or [
                {
                    "attribute_id": 0,
                    "website_id": 0,
                    "value": 0,
                    "website_value": 0,
                    "extension_attributes": {}
                }
            ],
            "configurable_product_options": data.get("extension_attributes").get("configurable_product_options") or [
                {
                    "id": 0,
                    "attribute_id": "product attribute_id",
                    "label": "product label",
                    "position": 0,
                    "is_use_default": True,
                    "values": [
                        {
                            "value_index": 0,
                            "extension_attributes": {}
                        }
                    ],
                    "extension_attributes": {},
                    "product_id": 0
                }
            ],
            "configurable_product_links": [
                0
            ]
        },
        "product_links": data.get("extension_attributes").get("product_links") or [
            {
                "sku": "product sku",
                "link_type": "product link_type",
                "linked_product_sku": "product linked_product_sku",
                "linked_product_type": "product linked_product_type",
                "position": 0,
                "extension_attributes": {
                    "qty": 0
                }
            }
        ],
        "options": data.get("extension_attributes").get("options") or [
            {
                "product_sku": "product product_sku",
                "option_id": 0,
                "title": "product title",
                "type": "product type",
                "sort_order": 0,
                "is_require": True,
                "price": 0,
                "price_type": "product price_type",
                "sku": "product sku",
                "file_extension": "product file_extension",
                "max_characters": 0,
                "image_size_x": 0,
                "image_size_y": 0,
                "values": [
                    {
                        "title": "product title",
                        "sort_order": 0,
                        "price": 0,
                        "price_type": "product price_type",
                        "sku": "product sku",
                        "option_type_id": 0
                    }
                ],
                "extension_attributes": {}
            }
        ],
        "media_gallery_entries": data.get("extension_attributes").get("media_gallery_entries") or [
            {
                "id": 0,
                "media_type": "product media_type",
                "label": "product label",
                "position": 0,
                "disabled": True,
                "types": [
                    "string"
                ],
                "file": "product file",
                "content": {
                    "base64_encoded_data": "product base64_encoded_data",
                    "type": "product type",
                    "name": "product name"
                },
                "extension_attributes": {
                    "video_content": {
                        "media_type": "product media_type",
                        "video_provider": "product video_provider",
                        "video_url": "product video_url",
                        "video_title": "product video_title",
                        "video_description": "product video_description",
                        "video_metadata": "product video_metadata"
                    }
                }
            }
        ],
        "tier_prices": data.get("extension_attributes").get("tier_prices") or [
            {
                "customer_group_id": 0,
                "qty": 0,
                "value": 0,
                "extension_attributes": {}
            }
        ],
        "custom_attributes": data.get("extension_attributes").get("custom_attributes") or [
            {
                "attribute_code": "product attribute_code",
                "value": "product value"
            }
        ]
    }

    # to prevent id error, so if **data dose not contain id, the json must not too.
    if not data.get("id"):
        del product_dict["id"]

    return json.dumps(product_dict)


def CreateProduct(site_url, sku, data, auth):
    response = requests.put('{}/rest/V1/products/{}'.format(site_url, sku), data=data, auth=auth,
                            headers={'Accept': 'application/json', 'Content-Type': 'application/json'})
    message_pattern = """
    {}
    status code : {}
    """

    # returning response message based on response status code.
    if response.status_code == 200:
        return message_pattern.format("Product Created Successfully", 200)
    elif response.status_code == 400:
        return message_pattern.format("Error : Bad Request", 400)
    elif response.status_code == 401:
        return message_pattern.format("Error : Unauthorized", 401)
    else:
        return message_pattern.format("Error : Unknown Error", response.status_code)
