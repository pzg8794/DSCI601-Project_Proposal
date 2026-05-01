# Artifact selection notes

The final presentation is designed to prioritize the strongest analysis artifacts from `presentation/analysis_artifacts/`.

Because the GitHub connector index available in this session did not expose the newly pushed directory listing, the deck uses a defensive LaTeX image-loading macro. Each evidence slide tries a list of likely artifact filenames first and falls back to a built-in TikZ/PGFPlots chart if none of those image files are present.

## Best figures to use

1. **Testing network / routing graph**
   - Best for explaining inefficient allocation due to missing vulnerability context.
   - Preferred slide placement: early clinical evidence section.

2. **Actual vs fair CMAB routing bar chart**
   - Best for showing the research contribution directly: the fair policy reverses the mismatch between burden and test access.
   - Preferred slide placement: immediately after the network graph.

3. **Pulse oximetry bias / occult hypoxemia graph**
   - Best for showing unreliable diagnostics due to missing calibration context.
   - Preferred slide placement: second clinical evidence case.

4. **Confusion matrix figure**
   - Best for turning the qualitative clinical story into evaluator metrics.
   - Preferred slide placement: after the two case-study graphs.

5. **Utility-fairness frontier**
   - Best for explaining why the project is not simply fairness versus performance, but better use of context.
   - Preferred slide placement: results or synthesis section.

## Expected filenames checked by the deck

The `.tex` source checks several names for each figure, including:

- `fig1_testing_network.pdf/png`
- `testing_network.pdf/png`
- `network_graph.pdf/png`
- `fig2_routing_counterfactual.pdf/png`
- `routing_counterfactual.pdf/png`
- `fair_cmab_routing.pdf/png`
- `fig3_pulseox_bias.pdf/png`
- `pulseox_bias.pdf/png`
- `occult_hypoxemia.pdf/png`
- `fig4_confusion_matrices.pdf/png`
- `confusion_matrices.pdf/png`
- `fig5_utility_fairness_frontier.pdf/png`
- `utility_fairness_frontier.pdf/png`

If your actual filenames differ, either rename the image files to one of these names or add the filename to the corresponding `\ShowArtifact` call in `final_presentation_draft2.tex`.
