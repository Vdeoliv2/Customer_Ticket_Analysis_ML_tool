# Day 35 — Interactive Support Dashboard

## Objective

The objective of Day 35 was to transform the historical customer-support analyses into an interactive Streamlit dashboard.

## Work Completed

I added an interactive Support Dashboard to the Streamlit application.

The dashboard includes filters for:

- Ticket Type
- Ticket Priority

The selected filters are applied to the original dataset to create a filtered DataFrame without modifying the original data.

The dashboard calculates and displays:

- Total Tickets
- Unresolved Tickets
- High-Priority Unresolved Tickets
- Average Customer Satisfaction
- Average Resolution Time

The dashboard also visualizes:

- Ticket Volume by Type
- Average Satisfaction by Type
- Average Resolution Time by Type

A detailed table displays the tickets matching the currently selected filters.

The application also checks whether a filter combination produces an empty dataset and displays a warning instead of attempting to calculate dashboard results.

## Dashboard Data Flow

df
→ user filters
→ filtered_df
→ KPI calculations
→ grouped analyses
→ charts and tables

## Conclusion

On Day 35, I expanded the Streamlit application by building an interactive Support Dashboard for exploring historical customer-support data.

Interactive Ticket Type and Ticket Priority filters allow the dashboard to create a filtered subset of the original dataset. The KPI calculations, visualizations, and ticket-detail table update based on this filtered data without modifying the original DataFrame.

The dashboard visualizes ticket volume, customer satisfaction, and resolution performance by Ticket Type. A detailed ticket table allows the user to inspect the records behind the aggregated metrics.

This stage converted the historical analyses developed earlier in the project into an interactive interface designed around the needs of a support manager.

The next step is to build the AI Ticket Analyzer for analyzing new customer-support tickets.
