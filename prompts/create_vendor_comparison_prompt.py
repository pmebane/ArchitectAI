def create_vendor_comparison_prompt(vendor_list):
    prompt = f"""How would somebody choose between {vendor_list[0]}, {vendor_list[1]}, and {vendor_list[2]}?
    """

    return prompt