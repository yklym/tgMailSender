def get_call_parameters(data: str, callback_name: str):
    name_list = callback_name.split('_')
    data_list = data.split('_')
    return [sub_str for sub_str in data_list if sub_str not in name_list]