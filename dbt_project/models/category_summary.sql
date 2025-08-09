select
  category,
  sum(amount) as total_amount,
  sum(quantity) as total_quantity
from {{ ref('staging_transactions') }}
group by category
order by category
