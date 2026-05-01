# Data notes

The CSV files in this directory are transparent aggregate inputs used to build the report figures. They combine cited public-health findings with clearly labeled scenario values for illustrating counterfactual fair routing.

No patient-level data, protected health information, or raw EHR data is included.

Files:

- `routing_inputs.csv`: aggregate values for COVID testing-access/routing figures.
- `pulseox_inputs.csv`: aggregate published pulse-oximetry bias values.
- `confusion_matrix_examples.csv`: explicit example matrices used for the explanatory confusion-matrix figure.

The report explains which values are directly sourced from literature and which values are counterfactual scenario outputs used to demonstrate how a fairness-aware contextual policy would be evaluated.
