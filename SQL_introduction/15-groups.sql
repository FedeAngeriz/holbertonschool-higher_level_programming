select score, count(*) AS number
from second_table
group by score
order by number desc;