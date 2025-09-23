# R-1.10 What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

range_parameters = range(8, -10, -2)
range_list = list(range_parameters)
print(
    "We need to send parameters: Start: 8; End: -10 (not inclusive); Step: -2\n",
    range_list,
)
