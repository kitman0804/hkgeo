from .API import API


OSM_DATA = {
    'HK': {
        'REGION': {
            'Hong Kong': ('relation', 913110), 
            'Hong Kong Island': ('relation', 2278450), 
            'Kowloon': ('relation', 2279652), 
            'New Territories': ('relation', 2279783)
        }, 
        'ISLAND': {
            'Hong Kong Island': ('relation', 3676781), 
            'Lantau Island': ('relation', 3676782)
        }
    }
}

__all__ = ['API']

