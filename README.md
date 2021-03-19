# Revenue Management - Retail Markdown Game Strategy

Revenue Management in the retail industry is comprised of a number of crucial factors such as budget, product price, and demand forecasting, and strategies outlining how to implement markdowns and where original prices should be reduced to increase sales over time. Unlike promotional discounts, which are mostly temporary and target customer-segment strategies, a markdown is when a retailer permanently lowers the price of a product with the intention of driving sales. Overbuying is one of the major concerns in the retail industry and markdowns are specifically used to eliminate this problem and increase revenue. This report employs The Retail Markdown Game to learn the best way to manage markdowns by testing out different algorithms. 
The outline for the Retail Markdown Game is as follows:

### Source Link: http://www.randhawa.us/games/retailer/nyu.html

### Objective: To develop a generic markdown pricing strategy for a retailer to maximize the total revenue when selling some inventory over a limited time period (i.e. at the end of week 15).

### Given Data:
• The initial stock is 2000 units
• The price is set at $60 for the first week
• The stock left-over at the end of the 15 weeks is lost i.e. there is no salvage value
• There are no other costs involved since the production costs for the items are already sunk

### The historical sales data provided (Sales-Data.xlsx) includes four columns:
• Week: The season from week 1 to week 15 (i.e. 14 decisions)
• Price: The price charged on a given week in $
• Sales: The amount sold on a given week
• Remaining Inventory: The inventory remaining at the end of the week

### Methodology:
1. Data Extraction, Pre-processing and Exploration
2. Developing Algorithms
	(A) Matrix Approach
	(B) Linear Optimization
	(C) Mean Difference Algorithm
3. Final Strategy 
4. Conclusion
