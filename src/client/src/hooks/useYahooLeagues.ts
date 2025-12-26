import { YahooService } from "@/services/YahooService";
import { useQuery } from "@tanstack/react-query";

export function useYahooLeagues() {
    const { data } = useQuery({
        queryKey: ['yahoo-leagues'],
        queryFn: YahooService.getLeagues
    });

    console.log(data)
    return data;
}