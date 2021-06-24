def inttoroman(nums):
    dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500:"D" , 1000: "M"}
    dict2 = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

inttoroman(2000)