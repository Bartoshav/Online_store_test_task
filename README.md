# Online_store_test_task
Creating an online store REST API with Django-rest-framework with following requirements:
1. Implement CRUD endpoint for the "Product" model with fields: Title - CharField, Price – DecimalField.
2. Implement CRUD endpoint for the "Order" model with fields: Date – DateField, Products - ManyToManyField(Product)	
3. List GET endpoints should be paginated
4. All endpoints should return JSON
5. Implement endpoint /api/stats. This endpoint should has input parameters: date_start/Date string: YYYY-MM-DD/Required, date_end/Date string: YYYY-MM-DD/Required, metric/Enum [‘price’, ‘count’]/Required. The response should contain a report with the monthly sales distribution for the selected period between date_start and date_end. If metric == “price” the value field should contain the total sum of all sold products in this month. If metric == “count” the value field should contain the total count of all sold products in this month.
5. Bonus objective: Setup Django-admin for the models
6. Bonus objective: Setup Swagger for the endpoints
