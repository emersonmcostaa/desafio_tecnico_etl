SELECT
  production_product."Name",
  production_product."DaysToManufacture",
  SUM(rox.sales_salesorderdetail."OrderQty") AS TotalSales
FROM
  rox.sales_SalesOrderDetail
  INNER JOIN rox.sales_specialofferproduct
    ON sales_salesorderdetail."ProductID" = sales_specialofferproduct."ProductID"
  INNER JOIN rox.production_product AS production_product
    ON sales_specialofferproduct."ProductID" = production_product."ProductID"
GROUP BY
  production_product."DaysToManufacture",
  production_product."Name"
ORDER BY
  TotalSales DESC
LIMIT 3;