def predict_disease(features):
    """
    Predict arecanut disease based on input features.
    
    Args:
        features (dict): Dictionary containing plant features
        
    Returns:
        tuple: (prediction, confidence)
    """
    # This is a simplified example. In a real model, you would use ML algorithms
    # like Random Forest, SVM, or Neural Networks to make predictions.
    
    # Example logic for different predictions based on features
    leaf_color = features['leaf_color'].lower()
    spot_color = features['spot_color'].lower()
    leaf_texture = features['leaf_texture'].lower()
    
    # Yellow Leaf Disease indicators
    if 'yellow' in leaf_color or 'yellowish' in leaf_color:
        prediction = "Yellow Leaf Disease"
        confidence = {'Yellow Leaf Disease': 75, 'Healthy': 25}
    
    # Koleroga (Fruit Rot) indicators
    elif 'black' in spot_color and ('soft' in leaf_texture or 'wet' in leaf_texture):
        prediction = "Koleroga Disease"
        confidence = {'Koleroga Disease': 80, 'Healthy': 20}
    
    # Bud Rot indicators
    elif 'brown' in leaf_color and 'wilting' in features['stem_condition'].lower():
        prediction = "Bud Rot Disease"
        confidence = {'Bud Rot Disease': 65, 'Healthy': 35}
    
    # Stem Bleeding indicators
    elif 'crack' in features['stem_condition'].lower() or 'oozing' in features['stem_condition'].lower():
        prediction = "Stem Bleeding"
        confidence = {'Stem Bleeding': 70, 'Healthy': 30}
    
    # Healthy plant
    elif 'green' in leaf_color and 'healthy' in features['stem_condition'].lower():
        prediction = "Healthy"
        confidence = {'Healthy': 90, 'Yellow Leaf Disease': 10}
    
    # Default case
    else:
        prediction = "Yellow Leaf Disease"  # Default prediction
        confidence = {'Yellow Leaf Disease': 60, 'Healthy': 40}
    
    return prediction, confidence