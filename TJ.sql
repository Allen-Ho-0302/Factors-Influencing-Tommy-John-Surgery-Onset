select distinct t.Player, t.Position, t.Throws, t.date_of_surgery, p.height, p.weight, datediff(day, p.debut, t.date_of_surgery) as daydiff
from TJ$ t
join People$ p
on t.Player=concat(nameFirst,' ',nameLast)
where p.height is not null and p.weight is not null and datediff(day, p.debut, t.date_of_surgery)>0 and datediff(day, p.debut, t.date_of_surgery)<7000
order by t.Player;