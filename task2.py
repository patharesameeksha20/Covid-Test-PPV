import numpy as np
import plotly.graph_objects as go

sensitivity = 0.99

specificity_list = [0.99, 0.999, 0.9999, 0.99999]

prevalence_list = np.geomspace(0.00001, 0.5, 300)

def calculate_ppv(prevalence, sensitivity, specificity):
    true_positive_rate = sensitivity * prevalence
    false_positive_rate = (1 - specificity) * (1 - prevalence)
    ppv = true_positive_rate / (true_positive_rate + false_positive_rate)
    return ppv

fig = go.Figure()

for specificity in specificity_list:
    ppv_values = []

    for prevalence in prevalence_list:
        ppv = calculate_ppv(prevalence, sensitivity, specificity)
        ppv_values.append(ppv * 100)

    fig.add_trace(
        go.Scatter(
            x=prevalence_list * 100,
            y=ppv_values,
            mode="lines",
            name=f"Specificity = {specificity * 100:.3f}%"
        )
    )

fig.update_layout(
    title="Probability Fred is infected after a positive test",
    xaxis_title="Infection prevalence (%)",
    yaxis_title="Probability infected given positive test (%)"
)

fig.update_xaxes(type="log")
fig.update_yaxes(range=[0, 100])

fig.show()

print("Integer check for prevalence = 5% and population = 100000")
print()

population = 100000
prevalence = 0.05

infected = int(population * prevalence)
not_infected = population - infected

for specificity in specificity_list:
    true_positives = int(infected * sensitivity)
    false_negatives = infected - true_positives

    true_negatives = int(not_infected * specificity)
    false_positives = not_infected - true_negatives

    ppv = true_positives / (true_positives + false_positives)

    print("Specificity:", specificity)
    print("Infected:", infected)
    print("Not infected:", not_infected)
    print("True positives:", true_positives)
    print("False negatives:", false_negatives)
    print("True negatives:", true_negatives)
    print("False positives:", false_positives)
    print("PPV:", round(ppv * 100, 2), "%")
    print()
