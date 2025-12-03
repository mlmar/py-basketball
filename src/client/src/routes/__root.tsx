import { Main } from '@/components/Main';
import { HomePage } from '@/features/HomePage';
import { Outlet, createRootRoute } from '@tanstack/react-router';

export const Route = createRootRoute({
    component: RootComponent,
    notFoundComponent: HomePage // Render home page by default
});

function RootComponent() {
    return (
        <Main>
            <Outlet />
        </Main>
    );
}
