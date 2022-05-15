#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import math
import statistics

values = []
coefficients = []

should_continue = True
should_break = False

while should_continue:
    value = input("Enter a value or 'end' to end: ")
    if value == 'end':
        break

    while not isinstance(value, int):
        try:
            value = int(value)
        except Exception:
            print("The value must be a number")
            value = input("Enter a value or 'end' to end: ")
            if value == 'end':
                should_break = True
                break
    if should_break:
        break

    coefficient = input(f"Enter the coefficient of the value '{value}': ")
    while not isinstance(coefficient, int):
        try:
            coefficient = int(coefficient)
        except Exception:
            print("The coefficient must be a number")
            coefficient = input(f"Enter the coefficient of the value '{value}': ")

    if value not in values:
        values.append(value)
        coefficients.append(coefficient)
    else:
        coefficients[values.index(value)] += coefficient


values_ = []
for index, value in enumerate(values):
    for loop in range(coefficients[index]):
        values_.append(value)

values_.sort()

mean = statistics.mean(values_)

quartiles = statistics.quantiles(values_, n=4)
first_quartile = quartiles[0]
median = statistics.median(values_)
third_quartile = quartiles[2]

harmonic_mean = statistics.harmonic_mean(values_)
geometric_mean = statistics.geometric_mean(values_)

variance = sum([(value-mean)**2 for value in values_]) / len(values_)
standard_deviation = math.sqrt(variance)

absolute_differences = [abs(value-mean) for value in values_]
mean_absolute_difference = sum(absolute_differences) / len(absolute_differences)
median_absolute_difference = statistics.quantiles(absolute_differences, n=2)[0]

scope = max(values_) - min(values_)

mode = statistics.mode(values_)

print("Mean / Moyenne ".ljust(49, '.') + f" : {mean}\n")

print("Harmonic mean / Moyenne harmonique ".ljust(49, '.') + f" : {harmonic_mean}")
print("Geometric mean / Moyenne géométrique ".ljust(49, '.') + f" : {geometric_mean}\n")

print("First quartile / Premier quartile ".ljust(49, '.') + f" : {first_quartile}")
print("Median / Médiane ".ljust(49, '.') + f" : {median}")
print("Third quartile / Troisième quartile ".ljust(49, '.') + f" : {third_quartile}\n")

print("Variance ".ljust(49, '.') + f" : {variance}")
print("Standard deviation / Écart-type ".ljust(49, '.') + f" : {standard_deviation}\n")

print("Mean absolute difference / Écart moyen absolu ".ljust(49, '.') + f" : {mean_absolute_difference}")
print("Median absolute difference / Écart médian absolu ".ljust(49, '.') + f" : {median_absolute_difference}\n")

print("Minimum value / Valeur minimum ".ljust(49, '.') + f" : {min(values_)}")
print("Maximum value / Valeur maximum ".ljust(49, '.') + f" : {max(values_)}")
print("Scope / Étendue ".ljust(49, '.') + f" : {scope}\n")

print("Mode ".ljust(49, '.') + f" : {mode}")
