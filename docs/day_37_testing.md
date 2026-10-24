# Day 37 --- Application Testing and Edge Cases

## Objective

The objective of Day 37 was to test the complete Streamlit prototype
under normal, invalid, unusual, and failure conditions.

Testing focused on the Overview page, Support Dashboard, and AI Ticket
Analyzer. The purpose was to verify that the application behaves
correctly and fails safely before deployment.

Tests that exposed problems were investigated, corrected when
appropriate, and retested.

### Test 1 --- Application Startup

**Expected:** The Streamlit application starts without an immediate
Python exception and displays the application interface.

**Observed:** The application started successfully and displayed the
Streamlit interface.

**Result:** PASS

### Test 2 --- Page Navigation

**Cases tested:** - Overview - Support Dashboard - AI Ticket Analyzer

**Expected:** Selecting each navigation option displays the
corresponding page.

**Observed:** All three navigation options displayed their corresponding
content.

**Result:** PASS

### Test 3 --- Overview Page

**Expected:** The application loads the cleaned dataset, displays the
dataset overview, and runs data validation.

**Observed:** The dataset loaded successfully and the Overview page
displayed the expected dataset information and validation result.

**Result:** PASS

### Test 4 --- Ticket Type Filter

**Input:** Technical Issue

**Expected:** Dashboard calculations, charts, and tables update to use
only tickets belonging to the selected Ticket Type.

**Observed:** The dashboard updated to show data for the selected Ticket
Type.

**Result:** PASS

### Test 5 --- Ticket Priority Filter

**Input:** High

**Expected:** Dashboard results update to include only the selected
priority.

**Observed:** The dashboard updated to show data for the selected Ticket
Priority.

**Result:** PASS

### Test 6 --- Combined Filters

**Ticket Type:** Technical Issue

**Ticket Priority:** High

**Expected:** Only tickets satisfying both selected filters are
included.

**Observed:** The dashboard updated to show data for the selected Ticket
Type and the selected Ticket Priority.

**Result:** PASS

### Test 7 --- Clearing Filters

**Expected:** Clearing all filters restores the unfiltered dashboard.

**Observed:** The dashboard updated to show the data for all the
tickets.

**Result:** PASS

### Test 8 --- Empty Filter Result

**Expected:** A zero-result filter combination should trigger the
empty-data warning.

**Observed:** No naturally occurring combination of the available Ticket
Type and Ticket Priority filters produced an empty dataset.

**Result:** NOT EXERCISED WITH CURRENT DATA

The application contains explicit empty-DataFrame handling, but this
branch could not be triggered using the available filter combinations.

### Test 9 --- Total Tickets KPI

**Filters:** Ticket Type: Technical Issue, Ticket Priority: High

**Expected:** Total Tickets equals the number of rows in the filtered
dataset.

**Expected calculation:** `len(filtered_df)`

**Observed dashboard value:** 458

**Observed filtered row count:** 458

**Result:** PASS

### Test 10 — Unresolved Tickets KPI

**Expected:** The KPI counts all unresolved tickets within the currently
filtered dataset.

**Observed:** With Ticket Type set to Technical Issue and Ticket Priority
set to High, the dashboard reported 301 unresolved tickets.

**Verification:** The filtered source data contained 301 tickets satisfying
the application's unresolved-ticket condition.

**Result:** PASS


### Test 11 — Unresolved Priority Breakdown

**Original Design:** The dashboard displayed a "High-Priority Unresolved"
KPI that combined High and Critical priorities.

**Problem Observed:** When the dashboard was filtered to High priority,
the Unresolved Tickets and High-Priority Unresolved values were identical.
When filtered to Critical, the same redundancy occurred because the
"High-Priority" calculation also included Critical tickets. Low-priority
filters produced zero for the High-Priority Unresolved KPI.

**Interpretation:** The calculation itself was functioning as programmed,
but the KPI design was redundant when a single priority was selected.
The label also obscured the distinction between High and Critical
priorities.

**Correction:** The combined High-Priority Unresolved KPI was replaced
with two separate KPIs:
- High Unresolved
- Critical Unresolved

The general Unresolved Tickets KPI was retained so that the dashboard
continues to show the total unresolved workload.

**Retest:** The corrected dashboard was tested using separate High and
Critical priority filters.

With Ticket Type set to Cancellation Request and Ticket Priority set to
High, the dashboard reported 274 Unresolved Tickets, 274 High Unresolved
tickets, and 0 Critical Unresolved tickets.

With Ticket Type set to Cancellation Request and Ticket Priority set to
Critical, the dashboard reported 278 Unresolved Tickets, 0 High Unresolved
tickets, and 278 Critical Unresolved tickets.

The results confirm that High and Critical unresolved tickets are now
counted separately and that each KPI responds correctly to the active
priority filter.

**Final Result:** PASS AFTER FIX
### Test 12 --- Average Satisfaction KPI

**Expected:** Average satisfaction is calculated from the currently
filtered tickets.

**Dashboard value:** 2.90

**Verification value recorded during testing:** 2.95862069

**Result:** RECHECK REQUIRED

**Reason:** 2.95862069 rounds to 2.96, not 2.90. The dashboard and
manual verification therefore do not currently agree. Recheck that the
same Ticket Type and Ticket Priority filters and the same rows are being
used before marking this test PASS.

### Test 13 --- Average Resolution Time

**Expected:** The dashboard calculates average resolution duration from
valid non-negative resolution durations in the currently filtered data.

**Dashboard value:** 7.44 hours

**Verification value recorded during testing:** 7.365191257 hours

**Result:** RECHECK REQUIRED

**Reason:** 7.365191257 rounds to 7.37 hours, not 7.44 hours. Recheck
that the manual verification uses the same filtered rows and the same
`Time to Resolution - First Response Time` calculation before marking
this test PASS.

### Test 14 --- Dashboard Charts

**Charts tested:** - Ticket Volume by Type - Average Satisfaction by
Type - Average Resolution Time by Type

**Expected:** Each chart updates when dashboard filters change.

**Observed:** All three charts updated according to the selected
filters.

**Result:** PASS

### Test 15 --- Ticket Detail Tables

**Expected:** Detail tables contain records consistent with the active
filters and their respective conditions.

**Observed:** The dashboard table matches the table obtained in the
original Excel data by applying the same filters.

**Result:** PASS

### Test 16 --- AI Testing

#### AI Test 16A --- Billing Example

**Input:** "I was charged twice for my monthly subscription."

**Expected application behavior:** The application completes both
analysis pipelines and displays the ML prediction and LLM analysis.

**ML prediction:** Product Inquiry

**LLM category:** Billing Inquiry

**LLM summary:** Charged twice for monthly subscription

**LLM sentiment:** Negative

**LLM urgency:** High

**Application completed without error:** YES

**Result:** PASS

#### AI Test 16B --- Refund Example

**Input:** "The item arrived damaged and I want my money back."

**Expected application behavior:** The application completes both
analysis pipelines and displays the ML prediction and LLM analysis.

**ML prediction:** Refund Request

**LLM category:** Refund Request

**LLM summary:** The item arrived damaged and I want my money back

**LLM sentiment:** Negative

**LLM urgency:** High

**Application completed without error:** YES

**Result:** PASS

#### AI Test 16C --- Cancellation Example

**Input:** "Please cancel my subscription before it renews."

**Expected application behavior:** The application completes both
analysis pipelines and displays the ML prediction and LLM analysis.

**ML prediction:** Billing Inquiry

**LLM category:** Cancellation Request

**LLM summary:** Customer wants to cancel subscription before renewal

**LLM sentiment:** Neutral

**LLM urgency:** High

**Application completed without error:** YES

**Result:** PASS

#### AI Test 16D --- Technical Example

**Input:** "The application crashes every time I try to log in."

**Expected application behavior:** The application completes both
analysis pipelines and displays the ML prediction and LLM analysis.

**ML prediction:** Refund Request

**LLM category:** Technical Issue

**LLM summary:** The application crashes every time I try to log in

**LLM sentiment:** Negative

**LLM urgency:** High

**Application completed without error:** YES

**Result:** PASS

#### AI Test 16E --- Inquiry Example

**Input:** "Does this product support Bluetooth?"

**Expected application behavior:** The application completes both
analysis pipelines and displays the ML prediction and LLM analysis.

**ML prediction:** Billing Inquiry

**LLM category:** Product Inquiry

**LLM summary:** Checking if a product supports Bluetooth

**LLM sentiment:** Neutral

**LLM urgency:** Low

**Application completed without error:** YES

**Result:** PASS

### Test 17 --- Blank Ticket

**Input:** Empty

**Expected:** The application displays a warning and does not execute
the analysis pipeline.

**Observed:** The application displayed the input warning and did not
attempt analysis.

**Result:** PASS

### Test 18 --- Whitespace-Only Ticket

**Input:** Spaces only

**Expected:** `.strip()` reduces the input to an empty string, causing
the same warning as a completely blank ticket.

**Observed:** The application displayed the input warning and did not
attempt analysis.

**Result:** PASS

### Test 19 --- Very Short Ticket

**Input:** "Help"

**Expected:** The application accepts the non-empty input and attempts
both analyses without crashing.

**ML prediction:** Refund Request

**LLM category:** Product Inquiry

**Observed behavior:** LLM creates a summary: "Customer seeking general
help"

**Result:** PASS

**Limitation observed:** Very short descriptions contain little context,
so classification results may not be meaningful.

### Test 20 --- Ambiguous Multi-Issue Ticket

**Input:** I cannot log into my account, I was charged again, and I want
to cancel the subscription and receive a refund.

**Expected application behavior:** Both pipelines should process the
ticket without crashing even though the description contains multiple
issues.

**ML prediction:** Billing Inquiry

**LLM category:** Refund Request

**Observed:** LLM showed a summary of "Customer is unable to log in, was
charged again, and wants to cancel and get a refund.", a negative
sentiment and a high urgency.

**Result:** PASS

**Interpretation:** This test demonstrates how the application behaves
when a ticket does not clearly belong to a single category.

### Test 21 --- Long Ticket Description

**Input length:** 173 characters

**Expected:** The application processes a substantially longer
description without interface or analysis failure.

**Observed:** The application did not crash and presented all the
outputs without failure

**Result:** PASS

### Test 22 --- Punctuation and Special Characters

**Input:** "HELP!!! I was charged \$49.99 TWICE??? Order #12345 --
why?!"

**Expected:** Punctuation, currency symbols, numbers, and repeated
punctuation do not cause the analysis pipeline to fail.

**Observed:** The application pipeline did not fail.

**Result:** PASS

### Test 23 --- ML/LLM Disagreement

**Input:** I need help because I cancelled my account but the interface
shows it is still charging.

**ML prediction:** Cancellation Request

**LLM prediction:** Billing Inquiry

**Expected application behavior:** The interface displays both
predictions without assuming that either one is correct.

**Observed:** Both predictions were displayed successfully.

**Result:** PASS

**Interpretation:** Disagreement between the classifiers is an expected
possibility and does not itself indicate an application failure.

### Test 24 --- LLM Service Unavailable

**Condition:** Ollama was intentionally stopped while the Streamlit
application remained running.

**Expected:** The LLM request should fail because the application cannot
connect to Ollama. The exception should be caught by the application's
error handler, and Streamlit should display an error message instead of
terminating the application.

**Observed:** The application displayed the following error message:
"Ticket analysis failed: Failed to connect to Ollama. Please check that
Ollama is downloaded, running and accessible.
https://ollama.com/download"

The Streamlit application remained available and could still be
navigated after the LLM request failed.

**Result:** PASS

**Interpretation:** The application's exception handling successfully
prevented an unavailable LLM service from crashing the Streamlit
application.

### Test 25 --- Malformed LLM JSON

**Expected:** If the LLM returns malformed JSON, JSON parsing may fail.
The resulting exception should be handled by the application's exception
handler.

**Observed:** No malformed JSON response occurred naturally during Day
37 testing.

**Result:** NOT OBSERVED

**Known Risk:** The application depends on the LLM returning valid JSON.
Malformed generated output could prevent the analysis from being parsed.

### Test 26 --- Missing LLM Fields

**Expected:** Successful LLM responses should contain Summary, Category,
Sentiment, and Urgency so that the interface can display all four
values.

**Observed:** All LLM responses observed during Day 37 testing contained
the four fields required by the interface.

No missing-field failure occurred naturally.

**Result:** NOT OBSERVED

**Known Risk:** Valid JSON could still be missing one or more fields
expected by the interface, which could cause an exception during
display.

### Test 27 --- Punctuation-Only Input Validation

**Inputs tested:** - "..." - "!!!???" - "123456"

**Expected:** Inputs containing no alphabetic characters should be
rejected before the traditional ML classifier or LLM analyzer executes.

**Original Observed Behavior:** The original validation did not
generalize to punctuation-only input. The application could accept input
such as "!!!???" and execute both analysis pipelines even though the
input did not contain meaningful ticket text.

**Original Result:** FAIL

**Cause:** The original input validation only used `.strip()` to check
whether the description was empty. The `.strip()` method removes
surrounding whitespace, but it does not remove or reject punctuation or
numbers.

**Correction:** The input-validation logic was expanded to require at
least one alphabetic character:

`any(character.isalpha() for character in cleaned_description)`

This prevents punctuation-only and numeric-only strings from reaching
the ML and LLM analysis pipelines.

**Retest Observed:** The inputs "...", "!!!???", and "123456" were all
rejected with the message "Please enter a meaningful ticket
description." Neither analysis pipeline executed.

**Retest Result:** PASS

**Final Result:** PASS AFTER FIX

### Test 28 --- Regression Test After Input-Validation Fix

**Input:** "I was charged \$49.99 twice for order #12345!"

**Expected:** The new validation should accept legitimate ticket
descriptions that contain letters together with numbers, currency
symbols, and punctuation.

**Observed:** The ticket passed input validation and both the
traditional ML classifier and LLM analyzer executed successfully.

**Traditional ML Prediction:** Product Inquiry

**LLM Category:** Billing Inquiry

**Result:** PASS

**Interpretation:** The validation correction successfully rejects
inputs containing no alphabetic text without preventing legitimate
ticket descriptions containing punctuation and numbers from being
analyzed.

### Test 29 --- LLM Recovery After Service Restart

**Condition:** Ollama was restarted after the LLM-unavailable test.

**Input:** "The application crashes every time I try to log in."

**Expected:** After restarting Ollama, the application should be able to
perform LLM analysis again.

**Observed:** The application successfully connected to Ollama and
displayed the LLM analysis after the service was restarted.

**LLM Category:** Technical Issue

**Result:** PASS

**Interpretation:** The temporary LLM service failure did not require
changes to the Streamlit application. Normal AI functionality resumed
after the external service became available again.

## Final Testing Summary

  --------------------------------------------------------------------------
  Area                       Result                  Notes
  -------------------------- ----------------------- -----------------------
  Application startup and    PASS                    All three pages opened
  navigation                                         successfully.

  Overview and dataset       PASS                    Dataset loaded and
  validation                                         validation executed.

  Dashboard filters          PASS                    Ticket Type, Ticket
                                                     Priority, combined
                                                     filters, and clearing
                                                     filters behaved
                                                     correctly.

  Empty-filter branch        NOT EXERCISED WITH      No available filter
                             CURRENT DATA            combination produced
                                                     zero rows.

  Total Tickets KPI          PASS                    Matched the filtered
                                                     row count.

  Unresolved Tickets KPI     PASS                    Matched the
                                                     unresolved-ticket
                                                     verification.

  Unresolved Rate KPI        RETEST AFTER UPDATE     Replaces the redundant
                                                     High-Priority
                                                     Unresolved KPI.

  Average Satisfaction KPI   RECHECK REQUIRED        Recorded dashboard and
                                                     verification values do
                                                     not agree.

  Average Resolution Time    RECHECK REQUIRED        Recorded dashboard and
  KPI                                                verification values do
                                                     not agree.

  Dashboard charts and       PASS                    Updated with filters
  detail tables                                      and matched filtered
                                                     records.

  Normal AI ticket           PASS                    ML and LLM pipelines
  processing                                         completed for the
                                                     tested ticket
                                                     categories.

  Blank and whitespace input PASS                    Analysis was prevented.

  Short, ambiguous, long,    PASS                    Application remained
  and special-character                              stable.
  input                                              

  ML/LLM disagreement        PASS                    Both predictions were
  display                                            shown without assuming
                                                     either was correct.

  LLM service unavailable    PASS                    Error was caught and
                                                     the Streamlit app
                                                     remained usable.

  Malformed LLM JSON         NOT OBSERVED            Remains a documented
                                                     risk.

  Missing LLM fields         NOT OBSERVED            Remains a documented
                                                     risk.

  Punctuation/numeric-only   PASS AFTER FIX          General
  validation                                         alphabetic-character
                                                     validation was added
                                                     and retested.

  Regression after           PASS                    Legitimate text
  validation fix                                     containing punctuation
                                                     and numbers still
                                                     worked.

  LLM recovery after restart PASS                    LLM analysis resumed
                                                     after Ollama restarted.
  --------------------------------------------------------------------------

## Day 37 Conclusion

Day 37 tested the complete Streamlit prototype under normal, invalid,
unusual, and external-service failure conditions. The testing covered
the Overview page, Support Dashboard, AI Ticket Analyzer, dashboard
filters, KPIs, charts, ticket tables, input validation, ML/LLM
disagreement, and Ollama availability.

Testing identified a genuine input-validation defect: `.strip()`
rejected blank or whitespace-only text but did not reject
punctuation-only or numeric-only input. The validation was expanded to
require at least one alphabetic character. The corrected behavior
rejected `"..."`, `"!!!???"`, and `"123456"`, while a legitimate ticket
containing letters, punctuation, numbers, and a currency value continued
to work.

Dashboard review also identified a design issue rather than a
calculation bug. The former `High-Priority Unresolved` KPI was redundant
whenever the Ticket Priority filter was set to High, because every
unresolved row in the filtered data was already High priority. Critical
tickets were included in the underlying urgent-priority logic, but the
label did not communicate that clearly. The dashboard was therefore
revised to use `Unresolved Rate` as the third KPI and to rename the
detailed table `Urgent Unresolved Tickets`, where urgent means High or
Critical and Critical remains the most urgent priority level.

The LLM-unavailable test also passed: when Ollama was stopped, the
application caught the connection exception and displayed an error
instead of crashing. Normal LLM functionality resumed after Ollama was
restarted.

Two KPI verification entries still require rechecking before the report
is fully final: Average Satisfaction and Average Resolution Time. Their
recorded manual verification values do not round to the values displayed
in the dashboard, so they should not be labeled PASS until the same
filters, rows, and calculations are confirmed.

After those two verification checks and the updated Unresolved Rate
retest, the application-testing stage is ready to close and the project
can proceed to deployment preparation.
