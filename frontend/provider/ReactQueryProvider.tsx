"use client"

import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ReactNode, useState } from "react";

// children : 어떤 컴포넌트 안에 넣은 다른 컴포넌트나 요소
// ReactQueryProvider라는 컴포넌트가 어떤 값을 전달받는지 정해주는 것
interface ReactQueryProviderProps {
    children: ReactNode
}

export default function ReactQueryProvider({children}: ReactQueryProviderProps) {

    const [queryClient] = useState(() => (
        new QueryClient({
            defaultOptions: {
                queries: {
                    staleTime: 1000 * 60 * 5, // 캐싱 5분 (데이터를 5분 동안 신선한 데이터로 취급한다는 뜻)
                    refetchOnWindowFocus: false // 윈도우 포커스시 refetching false
                    // (브라우저 창에 다시 포커스가 왔을 때 자동으로 데이터를 다시 가져오지 않도록 설정)
                }
            }
        })
    ))

    return (
        <QueryClientProvider client={queryClient}>
            {children}
        </QueryClientProvider>
    );
}