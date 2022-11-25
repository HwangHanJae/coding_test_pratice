select hour(datetime) as 'hour', count(hour(datetime)) as 'count'
from animal_outs
group by hour
having hour between 09 and 19
order by hour