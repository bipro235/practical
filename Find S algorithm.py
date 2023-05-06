#initialize the hyposthesis with most specific hypothesis
hypothesis = None

# Read the training examples
training_examples = [
    ('Sunny', 'Hot', 'High', 'Weak', 'No'),
    ('Sunny', 'Hot', 'High', 'Strong', 'No'),
    ('Overcast', 'Hot', 'High', 'Weak', 'Yes'),
    ('Rain', 'Mild', 'High', 'Weak', 'Yes'),
    ('Rain', 'Cool', 'Normal', 'Weak', 'Yes'),
    ('Rain', 'Cool', 'Normal', 'Strong', 'No'),
    ('Overcast', 'Cool', 'Normal', 'Strong', 'Yes'),
    ('Sunny', 'Mild', 'High', 'Weak', 'No'),
    ('Sunny', 'Cool', 'Normal', 'Weak', 'Yes'),
    ('Rain', 'Mild', 'Normal', 'Weak', 'Yes'),
    ('Sunny', 'Mild', 'Normal', 'Strong', 'Yes'),
    ('Overcast', 'Mild', 'High', 'Strong', 'Yes'),
    ('Overcast', 'Hot', 'Normal', 'Weak', 'Yes'),
    ('Rain', 'Mild', 'High', 'Strong', 'No')
]

# Iterate over each training examples
for examples in training_examples:
    
    # Split the data into attributes and target
    attributes, target = examples[:-1], examples[-1]
    
    # If the training examples is positive
    if target == 'Yes':
        
        # the hypothesis is None, initialize it with attributes
        if hypothesis is None:
            hypothesis = list(attributes)
        
        # Update the hypothesis finding the common value
        else:
            for i in range(len(attributes)):
                if hypothesis[i] != attributes[i]:
                    hypothesis[i] = '?'
                
print('Final hypothesis',hypothesis)

