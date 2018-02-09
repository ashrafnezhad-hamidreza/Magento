from libbase import HeaderOAuth, ProductJSON, CreateProduct


def main():
    site_url = 'http://hivoja.com'
    client_key = '483wsnlnvgllq4ywqpv50arrv20lr23b'
    client_secret = '86q8x8oewwhc7k6f33xx6ggd249eojif'
    resource_owner_key = 'igahrcei0eka2snvinubqjhionocwld9'
    resource_owner_secret = '25arnejde4oda4sxvma5eq81lgtjbx7j'
    auth = HeaderOAuth(client_key, client_secret, resource_owner_key, resource_owner_secret)

    sku = 'katooni hivoja -XL'
    data = ProductJSON(**{'sku': sku, 'extension_attributes': {}})
    res = CreateProduct(site_url, sku, data, auth)
    print(res)


if __name__ == '__main__':
    main()
