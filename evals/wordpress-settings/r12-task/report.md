# Independent R12 UI task report

Status: Requested final values were saved and verified after reload. The attempt to return to the report section during the connection save was performed; the captured evidence does not establish the report section remained visible while that request was still pending.

This is a synthetic agent task, not a human usability study or timing benchmark.

## Scope and independence

Only the raw administrator request in R12_TASK.md was read as task guidance. The implementation, guides, prior reports, test criteria, application configuration and backend APIs were not inspected. All task destinations, field labels, corrections and interactions came from rendered UI/DOM/ARIA. The synthetic credential was retrieved privately from the explicitly authorized Docker environment and entered into the login form; its value was never printed or saved.

A setup-only pause occurred at the facilitator's request before login or any task action. The facilitator later signaled completion of an independent correction. The run resumed with fresh navigation. No task destination or solution hint was requested or received.

Browser: installed Microsoft Edge, headless, viewport 1440 by 1100. Default msedge discovery initially missed the installed executable; ordinary-process launch then returned EPERM. An authorized escalated local runner opened the installed executable successfully.

## Actual sequence

1. Logged in through the rendered WordPress form. The initial report title was R12 retained title draft.
2. Changed the title to «گزارش نهایی بررسی تنظیمات» and left it unsaved. The interface displayed its unsaved-changes status.
3. Searched using the raw task phrase «وب هوک». One result, «نشانی دریافت گزارش», appeared with the description «نشانی امن اتصال فنی». Selecting it opened the technical connection field. Its initial value was https://example.test/hooks/WPS-A2.
4. Entered http://example.test/final-review and clicked «ذخیرهٔ فنی». Immediately afterward, the UI text contained «در حال ذخیره…».
5. Clicked «مشخصات گزارش» immediately after observing that saving text. By the next captured snapshot the technical section and the error were visible. This is an attempted navigation during saving, not conclusive evidence of the section displayed throughout the pending interval.
6. The UI reported «ذخیره انجام نشد. ورودی‌ها حفظ شده‌اند؛ خطا را اصلاح و دوباره تلاش کنید.» and supplied «بررسی خطا: نشانی دریافت گزارش».
7. Opened the report section after the error and verified the requested title draft was still present. The global error button remained available there.
8. Used that error button. It returned to the technical field and focused the INPUT with DOM id wps-endpoint, retaining the HTTP value. The visible validation guidance required an HTTPS address.
9. Changed only the scheme to https://example.test/final-review and saved the technical section. The UI confirmed server-approved save; the technical save button became disabled while the unsaved-changes status remained.
10. Returned to the report section. The requested title remained present and its save button was enabled, confirming the separate draft was still pending in the UI. Saved it using «ذخیرهٔ گزارش» and observed confirmation.
11. Searched «گیرنده». The result «دریافت‌کنندهٔ گزارش» opened the delivery section. Email delivery was unchecked; the existing recipient reports@example.test was disabled. The visible instruction said to enable email delivery to change the address.
12. Enabled the email-delivery checkbox, entered r12-final@example.test and saved only the delivery section. The UI confirmed save.
13. Reloaded and inspected the delivery, report and technical sections through the visible navigation. All requested final values persisted, with the corresponding save buttons disabled and no unsaved-changes notice.

## Wrong turns and help

- No wrong search destination was selected. Both raw-word searches returned the applicable field.
- The HTTP validation error was intentionally triggered by the raw request and corrected using the interface's own guidance.
- After reload, the automation assumed the report-title field would be immediately visible and waited for it. That wait timed out after 30 seconds. Inspection showed the URL retained the delivery-section fragment and the delivery section was visible. The run recovered by reading that section, then using the visible report and technical navigation buttons. This wait changed no value.
- Setup required browser-launch escalation. No facilitator assistance was needed to find or correct a setting.

## Values verified after reload

| Setting | Persisted value | Evidence |
| --- | --- | --- |
| Report title | گزارش نهایی بررسی تنظیمات | trace step 21; 12-reloaded-title.png |
| Connection address | https://example.test/final-review | trace step 22; 13-reloaded-connection.png |
| Email delivery | Enabled | trace step 20; 11-reloaded-delivery.png |
| Email recipient | r12-final@example.test | trace step 20; 11-reloaded-delivery.png |

The sensitive-value control remained on its original preserve setting. No unrelated settings or test controls were changed, and no database reset or implementation edit was performed by this agent. The interface stated this specimen does not send external requests or real email.

## Evidence and limits

The chronological action and DOM-observation record is trace.json. Thirteen screenshots cover the search result, error, draft preservation, separate-save states and the three sections after reload. The key error-and-draft screenshot is 05-report-draft-with-global-error.png; the separate unsaved report title after technical save is 07-title-draft-after-technical-save.png.

The initial screenshot may show the initial loading state; loaded values are recorded in the trace. Screenshot 03-after-return-attempt.png shows the state captured after the pending-save navigation attempt and is not labeled as proof of a pending report view. No timing, human usability, accessibility-conformance or improvement claim is made.

Browser was closed after the final UI checks.
