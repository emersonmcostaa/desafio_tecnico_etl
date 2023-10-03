SELECT
  "SalesOrderID",
  COUNT(*) AS number_of_details
FROM
  rox.sales_salesorderdetail
GROUP BY
  "SalesOrderID"
HAVING
  COUNT(*) >= 3;