
INSERT INTO public.pairing_suggestions (superior_id, interior_id)
SELECT 12 as superior_id, id as interior_id
FROM public.users
WHERE town = (SELECT town FROM public.users WHERE id = 12)
    AND sex = (SELECT sex_preference FROM public.users WHERE id = 12)
    AND sex_preference = (SELECT sex FROM public.users WHERE id = 12)
    AND active = TRUE
    AND NOT EXISTS (
        SELECT 1
        FROM public.pairing_suggestions
        WHERE superior_id = 12
          AND interior_id = interior_id
    )