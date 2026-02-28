from datetime import date

letter = ''' Dear <|Name|>,
            you are selected
              <|Date|>  '''

# Replace with values
letter = letter.replace("<|Name|>", "Harry")
letter = letter.replace("<|Date|>", str(date.today()))

print(letter)
