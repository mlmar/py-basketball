import { Config } from '@/services/Config';
import { redirect, createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/logout')({
    beforeLoad: () => {
        throw redirect({
            href: `${Config.SERVER_URL}/logout`
        });
    }
});
