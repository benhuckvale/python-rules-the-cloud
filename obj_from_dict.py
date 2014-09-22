
def obj_from_dict(root_dict, root_key="unnamed_obj"):
    """Takes a nested dictionary and converts it into an object tree."""
    def remap_to_obj(key, child_dict):
        if type(child_dict)==list:
            return [remap_to_obj(key, c) for c in child_dict]
        try:
            d={k: remap_to_obj(k, v) for k,v in child_dict.items()}
            d["as_dict"]=child_dict
            return type(key.encode("ascii", "ignore"), (object,), d)
        except AttributeError:
            return child_dict

    return remap_to_obj(root_key, root_dict)

