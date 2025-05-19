def create_pie_chart(confidence):
    """
    Create a pie chart HTML for the confidence values.
    
    Args:
        confidence (dict): Dictionary with disease names as keys and confidence percentages as values
        
    Returns:
        str: HTML for the pie chart
    """
    # This is a simplified example using Chart.js
    labels = list(confidence.keys())
    values = list(confidence.values())
    
    colors = []
    for label in labels:
        if label == 'Healthy':
            colors.append('rgba(72, 187, 120, 0.8)')  # Green for healthy
        elif label == 'Yellow Leaf Disease':
            colors.append('rgba(236, 201, 75, 0.8)')  # Yellow for Yellow Leaf Disease
        elif label == 'Koleroga Disease':
            colors.append('rgba(34, 139, 230, 0.8)')  # Blue for Koleroga
        elif label == 'Bud Rot Disease':
            colors.append('rgba(237, 100, 166, 0.8)')  # Pink for Bud Rot
        elif label == 'Stem Bleeding':
            colors.append('rgba(229, 62, 62, 0.8)')   # Red for Stem Bleeding
        else:
            colors.append('rgba(160, 174, 192, 0.8)')  # Gray for others
    
    chart_html = f"""
    <canvas id="confidenceChart"></canvas>
    <script>
        const confidenceCtx = document.getElementById('confidenceChart').getContext('2d');
        const confidenceChart = new Chart(confidenceCtx, {{
            type: 'pie',
            data: {{
                labels: {labels},
                datasets: [{{
                    data: {values},
                    backgroundColor: {colors},
                    borderColor: {colors},
                    borderWidth: 1
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        position: 'right',
                    }},
                    tooltip: {{
                        callbacks: {{
                            label: function(context) {{
                                return `${{context.label}}: ${{context.raw}}%`;
                            }}
                        }}
                    }}
                }}
            }}
        }});
    </script>
    """
    return chart_html

def create_bar_chart(features):
    """
    Create a bar chart HTML for feature importance.
    
    Args:
        features (dict): Dictionary with feature names and values
        
    Returns:
        str: HTML for the bar chart
    """
    # This is a simplified example - in a real application, you would calculate
    # actual feature importance values from your model
    
    # Dummy feature importance values
    feature_importance = {
        'leaf_color': 0.85,
        'spot_color': 0.78,
        'leaf_texture': 0.65,
        'stem_condition': 0.45,
        'soil_type': 0.70,
        'moisture_level': 0.80
    }
    
    labels = list(feature_importance.keys())
    values = list(feature_importance.values())
    
    # Make labels more readable
    readable_labels = [label.replace('_', ' ').title() for label in labels]
    
    chart_html = f"""
    <canvas id="featureChart"></canvas>
    <script>
        const featureCtx = document.getElementById('featureChart').getContext('2d');
        const featureChart = new Chart(featureCtx, {{
            type: 'bar',
            data: {{
                labels: {readable_labels},
                datasets: [{{
                    label: 'Feature Importance',
                    data: {values},
                    backgroundColor: 'rgba(72, 187, 120, 0.7)',
                    borderColor: 'rgba(72, 187, 120, 1)',
                    borderWidth: 1
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                scales: {{
                    y: {{
                        beginAtZero: true,
                        max: 1,
                        title: {{
                            display: true,
                            text: 'Importance Score'
                        }}
                    }},
                    x: {{
                        title: {{
                            display: true,
                            text: 'Features'
                        }}
                    }}
                }},
                plugins: {{
                    legend: {{
                        display: false
                    }},
                    tooltip: {{
                        callbacks: {{
                            label: function(context) {{
                                return `Importance: ${{(context.raw * 100).toFixed(0)}}%`;
                            }}
                        }}
                    }}
                }}
            }}
        }});
    </script>
    """
    return chart_html