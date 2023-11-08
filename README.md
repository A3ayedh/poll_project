# poll_project

## Bonus 
1. I found and intresting field name name db_comment its new in django. models.DateTimeField(db_comment="Date and time when the article was published",)  so i added it on Response class which you see the result in response part.

2. Another one is (verbose_name) which takes an optional first positional argument – a verbose name. If the verbose name isn’t given, Django will automatically create it using the field’s attribute name, converting underscores to spaces. So, I add on active_until field.

3. We add these part:
1. (In the poll question list, display a column showing the number of responses for the question)
1. (Create InlineModelAdmin for Poll and Option which allows editing and creating of the question and options in the same form)

4. Admin interface explore:
1. We got TabularInLine
1. And inlines in PostAdmin