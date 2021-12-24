SELECT gov_number, prime_min, start_date, recommendation.recommendation_id recommendation_id, recommendation_date, recommendation_desc
FROM government, recommendation
where government.recommendation_id =  recommendation.recommendation_id;

select party.name party_name, ideology_name
from party natural inner join party_ideology natural inner join ideology;

select party_id, name, seats, position_description
from party, position
where party.position_id = position.position_id;