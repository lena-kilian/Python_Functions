import copy as cp

# Change format of pandas.DataFrame from wide to long format
# new_var_1 and _2 are names or new variables and need to be entered as strings
# old_var_list must be a list of column names (as strings) to be converted e.g. old_var_list = ['variable1', 'variable2', 'variable3']
def wide_to_long(df, new_var_1, new_var_2, old_var_list):
    new_df = df.drop(old_var_list[1:], axis=1).rename(columns = {old_var_list[0]:new_var_2})
    new_df[new_var_1] = old_var_list[0]
    var_list_fl = cp.copy(old_var_list[1:])
    for value in var_list_fl:
        var_list_temp = cp.copy(old_var_list)
        var_list_temp.remove(value)
        df_temp = df.drop(var_list_temp, axis=1).rename(columns = {value:new_var_2})
        df_temp[new_var_1] = value
        new_df = new_df.append(df_temp, ignore_index = True)
    return(new_df)
    
# Change format of pandas.DataFrame from long to wide format
# headers is the name (as a string) of the column which contains future column names
# values is the name (as a string) of the column which contains future observations
def long_to_wide(df, headers, values):
    new_df = df.drop([headers, values], axis=1).drop_duplicates()
    merge_cols = new_df.columns.to_list()
    name_list = df[[headers]].drop_duplicates()[headers].to_list()
    for name in name_list:
        temp_df = df.loc[df[headers] == name].rename(columns={values:name}).drop(headers, axis=1)
        new_df = new_df.merge(temp_df, on=merge_cols, how='left')
    return(new_df)