param_grid = {
    "n_estimators":[3,10,30],
    "max_features":[2,4,6,8]
}

print(param_grid['n_estimators'][::2])
print(param_grid['max_features'][1::2])