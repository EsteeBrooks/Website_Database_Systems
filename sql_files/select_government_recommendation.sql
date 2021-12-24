SELECT gov_number, prime_min, start_date, recommendation.recommendation_id recommendation_id, recommendation_date, recommendation_desc
FROM government, recommendation
where government.recommendation_id =  recommendation.recommendation_id;
