import Link from "next/link";
import Image from "next/image";
import logoDark from "@/public/assets/images/header/logo.svg"
import logoWhite from "@/public/assets/images/header/logo-w.svg"

export default function Footer() {
    return (
        <footer className="flex justify-center bg-linear-to-b from-[#0E1A2E] to-[#07101F] h-170 px-[5%]">
            <div className="relative flex justify-between py-[90px] max-w-[1440px] w-full">
                <Link href="#">
                    <Image src={logoWhite} alt="" />
                    <p className="text-[#ACBBD0] pt-5">창업, 데이터로 먼저 확인하세요.</p>
                </Link>

                <ul className="flex w-full max-w-[650px] text-white">
                    <li className="w-full">
                        <p className="text-[17px] font-semibold text-[#5EF0DC] mb-5">서비스</p>
                        <ul className="flex flex-col gap-2 text-[#ACBBD0]">
                            <li><Link href="#">서비스 소개</Link></li>
                            <li><Link href="#">상권 분석</Link></li>
                            <li><Link href="#">지원사업 매칭</Link></li>
                            <li><Link href="#">기획서 AI 분석</Link></li>
                            <li><Link href="#">커뮤니티</Link></li>
                        </ul>
                    </li>
                    <li className="w-full">
                        <p className="text-[17px] font-semibold text-[#5EF0DC] mb-5">데이터 출처</p>
                        <ul className="flex flex-col gap-2 text-[#ACBBD0]">
                            <li><Link href="#">소상공인시장진흥공단</Link></li>
                            <li><Link href="#">서울시 상권분석서비스</Link></li>
                            <li><Link href="#">한국부동산원</Link></li>
                        </ul>
                    </li>
                    <li className="w-full">
                        <p className="text-[17px] font-semibold text-[#5EF0DC] mb-5">안내</p>
                        <p className="flex flex-col gap-2 text-[#ACBBD0]">데이터 기준일 2026.10</p>
                    </li>
                </ul>

                <span className="absolute left-0 bottom-[50px] text-[220px] text-white opacity-20 font-outfit font-bold">
                    Start 
                    <span className="text-[#5EF0DC]">Fit</span>
                </span>
            </div>
        </footer>
    );
}