import numpy as np
import plotly.graph_objects as go

sensitivity = 0.99

specificity_list = [0.99, 0.999, 0.9999, 0.99999]

prevalence_list = np.geomspace(0.00001, 0.5, 300)

def calculate_ppv(prevalence, sensitivity, specificity):
    true_positive = sensitivity * prevalence
    false_positive = (1 - specificity) * (1 - prevalence)
    ppv = true_positive / (true_positive + false_positive)
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
