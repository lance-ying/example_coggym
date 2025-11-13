# Ying et al. (2025) Understanding Epistemic Language with a Language-Augmented Bayesian Theory of Mind.

## Abstract
How do people understand and evaluate claims about others' beliefs, even though these beliefs cannot be directly observed? In this paper, we introduce a cognitive model of epistemic language interpretation, grounded in Bayesian inferences about other agents' goals, beliefs, and intentions: a language-augmented Bayesian theory-of-mind (LaBToM). By translating natural language into an epistemic ``language-of-thought'' with grammar-constrained LLM decoding, then evaluating these translations against the inferences produced by inverting a generative model of rational action and perception, LaBToM captures graded plausibility judgments of epistemic claims. We validate our model in an experiment where participants watch an agent navigate a maze to find keys hidden in boxes needed to reach their goal, then rate sentences about the agent's beliefs. In contrast with multimodal LLMs (GPT-4o, Gemini Pro) and ablated models, our model correlates highly with human judgments for a wide range of expressions, including modal language, uncertainty expressions, knowledge claims, likelihood comparisons, and attributions of false belief.

## Overview
- Cleaned stimuli and human response data for replicating the experiments from Ying et al. (2025).
- Organized into two experiments (`exp1`, `exp2`) with corresponding configuration, instruction, stimuli, and human response files.
- Assets include GIF/PNG stimulus renderings grouped by trial identifiers.

## Directory Structure
- ``exp1/``: Experiment with initial belief condition.
- ``exp2/``: Experiment with current belief condition.
