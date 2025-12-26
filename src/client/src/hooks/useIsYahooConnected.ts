import { YahooService } from "@/services/YahooService";
import { useQuery } from "@tanstack/react-query";

export function useIsYahooConnected(): boolean {
    const { data, isError } = useQuery({
        queryKey: ['validate-yahoo-user'],
        queryFn: YahooService.validateUser
    });

    return Boolean(data) && !isError;
}