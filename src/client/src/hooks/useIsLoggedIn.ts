import { AuthService } from "@/services/AuthService";
import { useQuery } from "@tanstack/react-query";

export function useIsLoggedIn(): boolean {
    const { data, isError } = useQuery({
        queryKey: [],
        queryFn: AuthService.validateUser
    });

    return Boolean(data) && !isError;
}