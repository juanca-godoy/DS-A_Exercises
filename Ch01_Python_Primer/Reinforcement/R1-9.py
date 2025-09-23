# R-1.9 What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?

range_parameters = range(50, 90, 10)
range_list = list(range_parameters)
print(
    "We need to send parameters: Start: 50; End: 90 (not inclusive); Step: 10",
    range_list,
)
